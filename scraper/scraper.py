import os, re, json, time, hashlib
from pathlib import Path
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from slugify import slugify
import trafilatura

BASE = "https://www.bibliotecapleyades.net/"
DATA_DIR = Path(__file__).resolve().parents[1] / "data"
ART_DIR  = DATA_DIR / "articles"
INDEX    = DATA_DIR / "index.json"
TIMEOUT  = 30

ART_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)

def fetch(url):
    r = requests.get(url, timeout=TIMEOUT, headers={"User-Agent": "Mozilla/5.0 (archiver)"})
    r.raise_for_status()
    return r.text

def discover_article_links():
    # Many sections use index pages ending with /indice_*.htm or /index.htm
    # We’ll crawl the home page and follow internal links, collecting *.htm/*.html
    seen, to_visit, articles = set(), [BASE], set()
    domain = urlparse(BASE).netloc

    def is_internal(u):
        p = urlparse(u)
        return p.netloc == "" or p.netloc == domain

    while to_visit:
        url = to_visit.pop()
        if url in seen: continue
        seen.add(url)
        try:
            html = fetch(url)
        except Exception:
            continue
        soup = BeautifulSoup(html, "lxml")

        # collect candidate pages
        for a in soup.select("a[href]"):
            href = a.get("href")
            if not href: continue
            absu = urljoin(url, href)
            if not is_internal(absu): continue
            if not absu.startswith(BASE): continue
            # keep only HTML pages
            if not re.search(r"\.(?:html?|shtml)$", absu, re.I):
                continue
            # Skip obvious nav assets
            if any(x in absu.lower() for x in ["/images/", "/img/", "/js/", "/css/"]):
                continue

            # Heuristic: treat leaf pages not obviously index-like as articles
            if not re.search(r"(index|indice|contents)\.html?$", absu, re.I):
                articles.add(absu)

            # BFS-ish: also crawl further (limits)
            if len(seen) < 4000 and len(to_visit) < 8000:
                to_visit.append(absu)

        # politeness
        time.sleep(0.1)

    return sorted(articles)

def extract_main_text(url, html):
    # Try robust auto-extraction first
    downloaded = trafilatura.extract(html, url=url, include_tables=False, include_comments=False)
    if downloaded and downloaded.strip():
        return downloaded

    # Fallback: simple main-content grab
    soup = BeautifulSoup(html, "lxml")
    # Try common containers
    candidates = [
        "#content", "#main", ".content", ".post", ".entry", "td[width='600']", "td[width='650']",
        "table table table"  # many legacy layouts
    ]
    for sel in candidates:
        node = soup.select_one(sel)
        if node and node.get_text(strip=True):
            return node.get_text("\n", strip=True)
    # last resort
    return soup.get_text("\n", strip=True)

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

def write_article(url, title, text):
    slug = slugify(title)[:120] or slugify(urlparse(url).path)[:120] or "article"
    sha = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    fname = f"{slug}-{sha}.md"
    path = ART_DIR / fname
    md = f"# {title}\n\n> Source: {url}\n\n{text}\n"
    path.write_text(md, encoding="utf-8")
    return str(path.relative_to(DATA_DIR))

def load_index():
    if INDEX.exists():
        return json.loads(INDEX.read_text(encoding="utf-8"))
    return {"generated_at": None, "articles": []}

def save_index(idx):
    idx["generated_at"] = int(time.time())
    INDEX.write_text(json.dumps(idx, ensure_ascii=False, indent=2), encoding="utf-8")

def main():
    idx = load_index()
    existing = {a["url"]: a for a in idx["articles"]}

    links = discover_article_links()
    print(f"Discovered {len(links)} candidate articles")

    updated = False
    for url in links:
        if url in existing:
            continue
        try:
            html = fetch(url)
            meta = meta_from_html(url, html)
            body = extract_main_text(url, html)
            # Skip very short bodies
            if not body or len(body.split()) < 80:
                continue
            relpath = write_article(url, meta["title"], body)
            entry = {
                "url": url,
                "title": meta["title"],
                "path": relpath,
                "word_count": len(body.split()),
                "added_at": int(time.time())
            }
            idx["articles"].append(entry)
            updated = True
            print(f"Added: {url}")
            time.sleep(0.2)
        except Exception as e:
            print("ERR", url, e)
            continue

    # sort by title for stability
    idx["articles"].sort(key=lambda x: x["title"].lower())
    if updated:
        save_index(idx)
        print("Index updated.")
    else:
        print("No new articles.")

if __name__ == "__main__":
    main()
