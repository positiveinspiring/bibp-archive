# Several Top Websites Use Device Fingerprinting to Secretly Track Users

> Source: https://www.bibliotecapleyades.net/SOCIOPOLITICA/sociopol_internet164.htm

by Staff Writers
Leuven, Belgium (SPX)
October 15, 2013
from
SpaceWar Website
A new study by KU Leuven-iMinds researchers has uncovered that 145 of the
Internet's 10,000 top websites track users without their knowledge or
consent.
The websites use hidden scripts to extract a
device fingerprint from users' browsers. Device fingerprinting circumvents
legal restrictions imposed on the use of cookies and ignores the Do Not
Track HTTP header.
The findings suggest that secret tracking is
more widespread than previously thought.
Device fingerprinting, also known as browser fingerprinting, is the practice
of collecting properties of PCs, smartphones and tablets to identify and
track users. These properties include the screen size, the versions of
installed software and plugins, and the list of installed fonts.
A 2010 study by the Electronic Frontier Foundation (EFF) showed that,
for the vast majority of browsers, the combination of these properties is
unique, and thus functions as a 'fingerprint' that can be used to track
users without relying on cookies.
Device fingerprinting targets either Flash, the
ubiquitous browser plugin for playing animations, videos and sound files, or
JavaScript, a common programming language for web applications.
This is the first comprehensive effort to measure the prevalence of device
fingerprinting on the Internet. The team of KU Leuven-iMinds researchers
analyzed the Internet's top 10,000 websites and discovered that 145 of them
(almost 1.5%) use Flash-based fingerprinting.
Some Flash objects included questionable techniques such as revealing a
user's original IP address when visiting a website through a third party (a
so-called proxy).
The study also found that 404 of the top 1 million sites use
JavaScript-based fingerprinting, which allows sites to track non-Flash
mobile phones and devices. The fingerprinting scripts were found to be
probing a long list of fonts - sometimes up to 500 - by measuring the width
and the height of secretly-printed strings on the page.
Do Not Track
The researchers identified a total of 16 new providers of device
fingerprinting, only one of which had been identified in prior research.
In another surprising finding, the researchers
found that users are tracked by these device fingerprinting technologies
even if they explicitly request not to be tracked by enabling the Do Not
Track (DNT) HTTP header.
The researchers also evaluated
Tor Browser and
Firegloves, two privacy-enhancing tools
offering fingerprinting resistance. New vulnerabilities - some of which give
access to users' identity - were identified.
Device fingerprinting can be used for various security-related tasks,
including fraud detection, protection against account hijacking and anti-bot
and anti-scraping services. But it is also being used for analytics and
marketing purposes via fingerprinting scripts hidden in advertising
banners and web widgets.
To detect websites using device fingerprinting technologies, the researchers
developed a tool called FPDetective. The tool crawls and analyses websites
for suspicious scripts. This tool will be
freely available here for other researchers
to use and build upon.
The findings will be presented at the
20th ACM Conference on Computer and
Communications Security this November in Berlin.
Top Sites (and maybe The NSA) Track Users with...
"Device Fingerprinting"
by Dan Goodin
October 11, 2013
from
ArsTechnica Website
May make it easier
to follow privacy-minded users
on the darknet.
Close to 1.5 percent of the Internet's top
websites track users without their knowledge or consent, even when visitors
have enabled their browser's Do Not Track option, according to an
academic research paper that raises new questions and concerns about online
privacy.
The research, by a team of scientists in Europe,
is among the first to expose the real-world practice of "device
fingerprinting," a process that collects the screen size, list of available
fonts, software versions, and other properties of the visitor's computer or
smartphone to create a profile that is often unique to that machine.
The researchers scanned select pages of the top
10,000 websites as ranked by Alexa and found that 145 of them deployed code
based on Adobe's Flash Player that fingerprinted users surreptitiously.
When they expanded their survey to the top one
million sites, they found 404 that used JavaScript-based fingerprinting.
The
researchers said the figures should be taken as the lower bounds since their
crawlers weren't able to access pages behind CAPTHCAs and other types of Web
forms.
Mainstream awareness of fingerprinting first
surfaced three years ago following the
release of research from the Electronic Frontier Foundation.
Device fingerprinting serves many legitimate
purposes, including mitigating the impact of denial-of-service attacks,
preventing fraud, protecting against account hijacking, and curbing content
scraping, bots, and other automated nuisances.
But fingerprinting also has a darker side.
For
one, few websites that include fingerprinting code in their pages disclose
the practice in their terms of service. For another, marketing companies
advertise their ability to use fingerprinting to identify user behavior
across websites and devices.
That suggests device fingerprinting may be used
much the way tracking cookies are used to follow people as they browse from
site to site, even though fingerprinting isn't covered by most laws
governing cookies and websites' Do Not Track policies.
And unlike user profiling that relies on "stateful"
browser cookies that are usually easy to delete from hard drives, most end
users have no idea that their computers are being fingerprinted, and they
have few recourses to prevent the practice.
"Device fingerprinting raises serious
privacy concerns for everyday users," the researchers wrote in a
recently published paper.
"Its stateless nature makes it hard to
detect (no cookies to inspect and delete) and even harder to opt-out.
Moreover, fingerprinting works just as well in the 'private-mode' of
modern browsers, which cookie-conscious users may be utilizing to
perform privacy-sensitive operations."
More troubling, device fingerprinting may have
given the National Security Agency (NSA) and its counterparts around the world an
avenue to identify people using the Tor privacy service.
As disclosed in an installment of previously
secret NSA documents published last week by The Guardian, the spy
agency is
capable of injecting script redirections into the traffic of Tor users.
Slide 16 of an
NSA presentation titled Tor Stinks included the excerpt:
"Goal: ...Ignore user-agents from Torbutton
or Improve browser fingerprinting? Using javascript instead of Flash?"
The Firefox browser that ships with the
Tor Browser
Bundle has long attempted to prevent fingerprinting by limiting the
customizable properties that are available to users.
It also placed a cap on the number of fonts a
webpage can request or load. The fingerprinting researchers found a way to
bypass the font cap by making use of the Web programming property known as
CSS
font face.
The researchers reported their findings to Tor
developers, who have since
patched the weaknesses.
Orbitz, T-Mobile, Western Union,
and Poker-Strategy among the players
The researchers said their lawyers advised them
not to provide an exhaustive list of the 404 or more websites that hosted
tracking code.
Responding to questions from Ars, researcher
Gunes Acar of
KU Leuven University
in Belgium said that they included,
-
orbitz.com
-
tmobile.co.uk
-
pokerstrategy.com
-
anonymizer.com
-
westernunion.com
-
t-online.de
He
stressed that his team may have missed some sites given the limitations of
their scanning technology.
Tracking code based on Adobe Flash is
particularly time consuming to detect because it must be decompiled and
manually analyzed.
As a result, the researchers scanned only 10,000
sites and limited the searches to homepages, even though some sites are
known to deploy tracking code on registration pages and other subsections.
Two of the few websites named in the paper are,
...both owned by
a company called Anonymizer Inc.
The former site offers a Java applet that
allows visitors to test how easy they are to track online. Before users can run it, the site discloses what
information will be gathered and warns,
"Data obtained from the browser like lists
of plug-ins or fonts can be used to identify your computer."
Anonymizer.com, in sharp contrast, ran largely the same fingerprinting
scripts on its homepage without making any mention that it was compiling
a list of fonts and plug-ins that could be used to identify an end
user's computer.
"Finally, note that while privacytool.org
offers informed choice to its users, who may voluntarily execute the
script, the fingerprinting scripts that run in the anonymizer.com
homepage are invisible to users and run by default," the researchers
reported.
Anonymizer.com representatives didn't respond to
messages seeking comment for this article.
Going mainstream
The researchers said many website operators may
have no idea that fingerprinting is taking place on the pages they maintain.
In one case, a font-probing script was embedded into a button users clicked
to donate bitcoins to the site owner.
The researchers uncovered 15 third-party
providers of fingerprinting services, with names including BlueCava,
Perferencement, CoinBase, and MaxMind.
"What surprised us was the variety of the
companies providing this service," Acar wrote in an e-mail to Ars.
"We knew it was used to secure
authentication for online banking or retail, but what we found out is
it's becoming mainstream. We even found that fingerprinting scripts are
embedded in widgets or ad banners."
He said end users who want to prevent their
systems from being fingerprinted have few options other than to run Tor.
Disabling JavaScript and Flash in the browser
reduces some of the information websites can collect, but it does nothing to
stop font probing, including the attack on older versions of the Tor
Browser.
What's more, disabling both Flash and JavaScript ironically creates
a configuration that rare. There are a variety of services that test test
how identifiable a specific browser is, including
this one from the EFF.
The paper - titled "FPDetective
-
Dusting the Web for Fingerprints" - will be presented next month at the
20th ACM Conference on
Computer and Communications Security in Berlin.
The research is important because it highlights
a practice that few people have any idea is taking place.
Readers shouldn't
view it as an indictment of fingerprinting itself or the websites that
engage in it. But it's fair to read the findings as clear evidence that
fingerprinting probably won't remain a nascent or niche practice for much
longer.
Websites that want visitors' trust should
disclose how and when fingerprinting is used and take steps to limit its
harm to user privacy.
