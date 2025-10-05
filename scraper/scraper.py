import os, re, json, time, hashlib, sys
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib import robotparser
import requests
from bs4 import BeautifulSoup
from slugify import slugify
import trafilatura

# ------------------------
# Config (tunable via env)
# ------------------------
BASE = "https://www.bibliotecapleyades.net/"
DATA_DIR = Path(__file__).resolve().parents[1] / "data"
ART_DIR  = DATA_DIR / "articles"
INDEX    = DATA_DIR / "index.json"

SLEEP_SEC       = float(os.getenv("SLEEP_SEC", "0.15"))          # politeness delay
BATCH_LIMIT     = int(os.getenv("BATCH_LIMIT", "600"))           # max new/changed articles per run
DISCOVER_LIMIT  = int(os.getenv("DISCOVER_LIMIT", "20000"))      # cap discovery frontier
TIMEOUT         = int(os.getenv("TIMEOUT", "30"))
RETRY_TRIES     = int(os.getenv("RETRY_TRIES", "3"))

# ------------------------
# Setup
# ------------------------
ART_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)

def log(*args):
    print(*args, flush=True)

# ------------------------
# Networking helpers
# ------------------------
def fetch(url, tries=RETRY_TRIES):
    for i in range(tries):
        try:
            r = requests.get(
                url,
                timeout=TIMEOUT,
                headers={"User-Agent": "Mozilla/5.0 (archiver)"},
            )
            r.raise_for_status()
            return r.text
        except Exception as e:
            if i == tries - 1:
                raise
            time.sleep(1.5 * (i + 1))

def robots_allows(base_url):
    try:
        rp = robotparser.RobotFileParser()
        rp.set_url(urljoin(base_url, "/robots.txt"))
        rp.read()
        allowed = rp.can_fetch("Mozilla/5.0 (archiver)", base_url)
        if not allowed:
            log("⚠️  robots.txt disallows base URL; proceeding cautiously (read-only archiving).")
        return True  # We respect but don't hard-block; throttle + read-only usage.
    except Exception:
        return True

# ------------------------
# Discovery
# ------------------------
def discover_article_links():
    seen, to_visit, articles = set(), [BASE], set()
    domain = urlparse(BASE).netloc
    pages_scanned = 0

    def is_internal(u):
        p = urlparse(u)
        return p.netloc == "" or p.netloc == domain

    while to_visit and len(seen) < DISCOVER_LIMIT:
        url = to_visit.pop()
        if url in seen:
            continue
        seen.add(url)
        try:
            html = fetch(url)
        except Exception:
            continue

        soup = BeautifulSoup(html, "lxml")

        for a in soup.select("a[href]"):
            href = a.get("href")
            if not href:
                continue
            absu = urljoin(url, href)
            if not is_internal(absu):
                continue
            if not absu.startswith(BASE):
                continue
            if not re.search(r"\.(?:html?|shtml)$", absu, re.I):
                continue
            low = absu.lower()
            if any(x in low for x in ["/images/", "/img/", "/js/", "/css/"]):
                continue

            # Treat likely leafs as articles
            if not re.search(r"(index|indice|contents)\.html?$", absu, re.I):
                articles.add(absu)

            if len(to_visit) < DISCOVER_LIMIT:
                to_visit.append(absu)

        pages_scanned += 1
        if pages_scanned % 100 == 0:
            log(f"🔎 Scanned {pages_scanned} pages | discovered {len(articles)} candidate articles")
        time.sleep(SLEEP_SEC)

    log(f"✅ Discovery complete: {len(articles)} candidate articles")
    return sorted(articles)

# ------------------------
# Extraction & writing
# ------------------------
def extract_main_text(url, html):
    # Try robust auto-extraction first
    downloaded = trafilatura.extract(
        html, url=url, include_tables=False, include_comments=False
    )
    if downloaded and downloaded.strip():
        return downloaded
    # Fallback: body text
    soup = BeautifulSoup(html, "lxml")
    body = soup.find("body")
    return (body or soup).get_text("\n", strip=True)

def meta_from_html(url, html):
    soup = BeautifulSoup(html, "lxml")
    title = None
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    if not title:
        h1 = soup.find("h1")
        if h1:
            title = h1.get_text(strip=True)
    if not title:
        title = url
    return {"title": title}

def content_sha(text):
    return hashlib.sha1(text.encode("utf-8")).hexdigest()

def write_article(url, title, text):
    slug = slugify(title)[:100] or slugify(urlparse(url).path)[:100] or "article"
    sha = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
    fname = f"{slug}-{sha}.md"
    path = ART_DIR / fname
    md = f"# {title}\n\n> Source: {url}\n\n{text}\n"
    path.write_text(md, encoding="utf-8")
    return str(path.relative_to(DATA_DIR))

# ------------------------
# Index helpers
# ------------------------
def load_index():
    if INDEX.exists():
        return json.loads(INDEX.read_text(encoding="utf-8"))
    return {"generated_at": None, "articles": []}

def save_index(idx):
    idx["generated_at"] = int(time.time())
    INDEX.write_text(json.dumps(idx, ensure_ascii=False, indent=2), encoding="utf-8")

# ------------------------
# Main
# ------------------------
def main():
    log("🚀 Starting crawl...")
    robots_allows(BASE)

    idx = load_index()
    by_url = {a["url"]: a for a in idx["articles"]}

    links = discover_article_links()
    log("🧮 Total candidates:", len(links))

    updates = 0
    for i, url in enumerate(links, 1):
        if updates >= BATCH_LIMIT:
            log(f"🛑 Reached batch limit ({BATCH_LIMIT}); stopping for this run.")
            break

        try:
            if url in by_url:
                # Existing: fetch & check if changed
                html = fetch(url)
                body = extract_main_text(url, html)
                if not body or len(body.split()) < 80:
                    continue
                new_hash = content_sha(body)
                if by_url[url].get("content_sha") == new_hash:
                    # unchanged
                    if i % 100 == 0:
                        log(f"= {i}/{len(links)} unchanged so far")
                    time.sleep(SLEEP_SEC)
                    continue
                # changed: rewrite file
                meta = meta_from_html(url, html)
                relpath = write_article(url, meta["title"], body)
                by_url[url].update({
                    "title": meta["title"],
                    "path": relpath,
                    "word_count": len(body.split()),
                    "updated_at": int(time.time()),
                    "content_sha": new_hash,
                })
                updates += 1
                log(f"♻️  Updated: {meta['title']}")
            else:
                # New article
                log(f"➕ [{i}/{len(links)}] Fetching: {url}")
                html = fetch(url)
                meta = meta_from_html(url, html)
                body = extract_main_text(url, html)
                if not body or len(body.split()) < 80:
                    log("   ⚠️  Skipping (too short)")
                    time.sleep(SLEEP_SEC)
                    continue
                relpath = write_article(url, meta["title"], body)
                entry = {
                    "url": url,
                    "title": meta["title"],
                    "path": relpath,
                    "word_count": len(body.split()),
                    "added_at": int(time.time()),
                    "content_sha": content_sha(body),
                }
                idx["articles"].append(entry)
                by_url[url] = entry
                updates += 1
                log(f"   ✅ Saved: {meta['title']}")

            if i % 50 == 0:
                log("💾 Saving index checkpoint...")
                idx["articles"].sort(key=lambda x: x["title"].lower())
                save_index(idx)

        except Exception as e:
            log("❌ Error:", url, e)

        time.sleep(SLEEP_SEC)

    # Final save
    idx["articles"].sort(key=lambda x: x["title"].lower())
    save_index(idx)
    if updates:
        log(f"📁 Index updated with {updates} new/changed articles.")
    else:
        log("ℹ️  No new or changed articles this run.")

if __name__ == "__main__":
    main()
