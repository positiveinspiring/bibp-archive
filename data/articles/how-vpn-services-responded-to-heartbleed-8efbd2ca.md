# How VPN Services Responded to Heartbleed

> Source: https://www.bibliotecapleyades.net/SOCIOPOLITICA/sociopol_internet188.htm

-
What steps has your company taken in
response to Heartbleed?
-
In your opinion, what were the risks users faced before these steps
were taken?
-
How did you communicate the above to your users?
1.
Heartbleed was an eye opener which helped to make the public more aware
of the insecurities that exist in un-audited code.
Regardless of being
open or closed source, there will always be insecurities in systems.
However, the best that companies can do is to strive to achieve 100%
security. In our case, when the Heartbleed exploit was announced, we
reacted immediately.
It was publicly disclosed at or about UTC 19:00:00
on April 7, 2014. We patched our VPN gateways within 4 hours at or about
UTC 23:17:15 on April 7, 2014 by upgrading our OpenSSL libraries to
version 1.0.1g from 1.0.1f.
Our website was not exploitable given that
we use a hardware load balancer that is not using a vulnerable version
of OpenSSL.
Immediately after patching our VPN gateways,
we then setup a non-production gateway that we attempted to exploit
using the Heartbleed exploit POCs (proof of concepts). While it was
recently announced that OpenVPN is exploitable, it is our best belief
that our private keys were never leaked given that we have systems in
place that make the exploitation of our servers very unlikely.
That being said, within 24 hours we are
rolling out updates to our clients as well, even though it is highly
unlikely that our keys were ever leaked.
2. The likeliness of our gateways being
exploited prior to us rolling out these patches are extremely low.
However, as stated earlier, at Private Internet Access, we strive to
achieve 100% security, so we went through the motions as it is our
policy to do so in best practice.
3. We waited to announce anything to our
users until we were 100% certain of everything we were stating. That
said, we
posted on our blog after we performed our patches.
Additionally, we will be sending out a mass
e-mail within 24 hours to our clients as certain users (DD-WRT, stock
OpenVPN, etc.) will need to manually apply updates in order to connect
to our service.
1.
Upon hearing of the OpenSSL vulnerability our staff took immediate
action to preserve the integrity and security of TorGuard services.
This
included a full audit of our VPN network, software, and websites. All
VPN servers have now been updated to a non vulnerable version of OpenSSL
and these new connections have been automatically downloaded in all TG
VPN clients.
TorGuard's Pro VPN client software has also been updated to
the latest patched OpenVPN version and pushed to all users. Our
company's website infrastructure, client area, and email services were
not vulnerable even in the months prior when this bug was out in the
wild.
2. While the threats posed by the OpenSSL
HeartBleed vulnerability are wide reaching and potentially very serious,
our team can confidently say this development had no impact on the
security of TorGuard's users. Rest assured, we won't let your heart
bleed.
3. TorGuard
posted the findings of the network audit on our blog and immediately
emailed all clients a direct link.
1.
Once the vulnerability was made public we instantly started to patch all
affected systems. This particular bug was present on our IPv6 VPN
machines, a subset of the IPv4 VPN servers that were using OpenSSL 1.0.1
and all of our external SSL services like the website, the tor exit
node, or jabber server.
After the upgrade to the latest OpenSSL
version was finished we decided to replace the private keys from all
affected components because the confidentiality of those keys could not
be guaranteed anymore. The window of opportunity for an attacker who had
this bug as a 0day up his/her/its sleeve was simply too long. Due to the
nature of the bug it is very difficult to say retrospectively if it was
used to gain access to possibly sensitive memory contents of the
affected machines.
Since we had to replace all affected VPN
server certificates we decided to deploy a new key management scheme for
those machines. Each OpenVPN instance now uses one time private keys,
cert and DH keys that are cycled on process restart.
In the same way we have seen the emergence
of special purpose hardware for Bitcoin mining we should also assume
that the entities that have the means to compromise cryptography also
possess special hardware to deal with encryption. As an additional
precaution against this scenario we deployed server and DH keys with
variable lengths instead of sticking to the "well known"
lengths/constants of 2048 and 4096 bit.
We are still working on making sure that all
OpenSSL 1.0.1 components support the EC curve 25519 from DJB since any
EC constants put forth by the NIST (or NSA) should be considered
compromised.
2. Total exposure.
3. Users were informed through the usual
channels (Twitter, blog, IRC).
1. We upgraded OpenSSL on all servers and client downloads. We created
new keys on all servers. We revoked all old keys. We released a new
client program with the revocation list that also creates new client
keys. For those not using our client program we published new OpenVPN
configuration files with the revocation list and new client keys for all
users.
2. It was unknown how vulnerable OpenVPN was
in practice so we decided to find out by trying to exploit the bug on a
test server. We repeatedly succeeded in extracting the server's private
key. These findings were sent in full detail to the OpenVPN team and
published in less harmful form e.g.
here.
The conclusion is that before the fixes
above all OpenVPN communication were at risk of decryption by anyone
knowing about the bug 'at the time'. Due to perfect forward secrecy they
can't be decrypted with a key leaked at a later time. So anyone who did
not know about the bug but managed to snatch a key after the bug was
published can't go back and decrypt traffic they may have stored.
3. We put a big red warning banner on our
website that is still there and published a news item explaining the
situation and urging all
users to upgrade.
1.
We learned about the vulnerability at 9:17PM CST on April 7th. From that
point forward, we did not sleep until the vulnerability was closed and
every server was penetration tested against all known forms of the
exploit to ensure that the vulnerability was closed.
At the time we found out about the
vulnerability, there wasn't even a CVE entry in the database explaining
the nature of the vulnerability or the attack. We knew that because of
the integration of OpenSSL into the Windows OpenVPN open-source client,
and the default builds of OpenSSL installed into almost all distros of
Linux/BSD that this was going to be huge.
As more information unfolded and the OpenSSL
updates hit the verified repositories, we began the patching process on
our servers. After the main vulnerability was closed and a rolling
restart was issued to the server clusters, we went to work with
notifying clients of the bug and advising them to update their clients
to current.
The servers were patched and confirmed safe
by 7:00AM CST on April 8th. This is when we released our transparency
post advising our users on the situation, and how they can respond to
close the bug client-side. A mass email was sent shortly after advising
our clients to read the post, and had instructions on updating their
clients.
2. The bug is catastrophic in scale. We
avoided disaster by having a very strong security model and not allowing
clients to change security settings. During the vulnerable period where
the bug was unknown publicly, there was no way for a VPN provider to
detect if they were attacked. It is possible that server keys and certs
were lost although we have had no evidence of this. Our root CA was not
exposed. Our website was unaffected. Our load-balancers were unaffected.
The worst case scenario for our security
topology is that keys and certs and the tls-auth server key were lost to
a nefarious attacker who was subscribed to the service. (because of
TLS-Auth, there was no way to exploit heartbleed from outside of the
network, only inside).
If this were to occur, an attacker could attempt
to impersonate a VPN server. In order for the attack to work they would
have to take many specific steps to circumvent various load-balancing
and routing steps that place during the connection process. We think
that this is highly unlikely to have happened, but is not impossible, so
we are disclosing it to be as open and transparent as possible.
Note that a VPN service that claims zero
exposure to Heartbleed is almost certainly lying or has so little
knowledge about network security that they should not be in the
business. Heartbleed hit everyone, it is a matter of how badly.
3. We responded publicly
here, and also also had a Heartbleed
article here. We also made informational posts to the community at
/r/VPN on Reddit and reached out to other VPN services we are close to
in order to discuss countermeasures and implementations. We also made an
effort
to educate the /r/VPN community on proper countermeasures.
1.
We revoked all VPN server certificates and generated new 4096 bit
certificates within a few hours of the announcement. We've also had our
websites EV certificate reissued. Most of our client software was not
using a vulnerable version of OpenVPN but where necessary we patched the
client software as well.
2. A successful attack could reveal the
server's private key which could be used to impersonate the server in a MITM attack or to passively decrypt the session keys during SSL
negotiation. Although we implement tls-auth this doesn't mitigate the
risk substantially since the auth keys are visible to all customers. Its
important to understand that a successful attack prior to the
announcement would likely only be possible from a very sophisticated and
well funded adversary targeting a specific individual. Such adversaries
almost certainly continue to possess undisclosed vulnerabilities that
they can use to exploit targets.
3. We sent out a tweet immediately after
installing the new certificates. We then emailed all our customers with
information about the vulnerability and instructions on how to update
the client software where required. We also
made an
infographic to help customers understand what passwords to change on
other services.
PrivatVPN
1. Yes, we have updated OpenSSL on both
OpenVPN servers and the website. The certificate for the VPN server has
been updated as well.
2. Hard to say. Worst case is that
information has been leaked when we had the old version of OpenSSL.
3. We
posted two
updates on our website.
1.
We constantly monitor all upstream software providers and keep current
with the upgrades they provide. As such, as soon as a fix was made
available that would suit our platform as well as our internal security
standards, we took all steps necessary to upgrade our systems.
Following a routine audit we've concluded
that none of our critical systems were affected during the period
between the public release of the proof of concept and the date at which
the necessary fixes were applied.
2. As our systems are being actively
monitored there is no reason to believe that our customers were affected
by the Heartbleed attack in any way. Since the exploit seems to work on
both server software and client software, there is a slight chance that,
if some of our users are also using other providers, they would be
affected in case a malicious provider - by choice or having been
affected themselves - were to attempt to extract information from them.
The information - from what we've seen in
the behavioral analysis of the exploit by various security professionals
- that they would be able to obtain would be pertinent only to their
specific connection to that provider. Also, from a client's perspective,
running a Windows machine the only service potentially affected by this
bug would be OpenVPN as the others are key services provided by
Microsoft in the core OS and do not share anything in common with the
OpenSSL library.
3. We constantly run security audits,
monitor our network and improve TigerVPN. Although the incident was
hyped on a big scale, we did a lot of upgrades, fixes and improvements
throughout the month. If we would inform our customers about every
single time we work on our software or hardware, they'd unsubscribe and
report us as spam.
We understand this is in the nature of our
responsibility to pro-actively react to events such as Heartbleed. In
case we ever noticed any kind of breach, all our customers would get
notified immediately as with a single click.
1.
Our website was running an unaffected version of OpenSSL (0.9.8g)
however we updated OpenSSL there anyway.
Some VPN servers were vulnerable so we
updated all servers on April 8th to protect against further attacks.
On April 17 we issued new VPN configs with
new 4096 bit certificates. We were working on this after we found out
about Heartbleed but as soon as it was proven that the bug can be used
against OpenVPN we immediately made the new configs + certificates
available to everyone. On the VPN server side all the certificates, keys
and DH keys have been replaced.
2. It has been proven that Heartbleed can be
used to steal the private key and impersonate a VPN server (if the VPN
server was running a vulnerable version of OpenSSL). People connecting
to what they thought was their real VPN provider could actually be
connecting to a fake VPN server or honeypot - although this would take
the resources of a powerful government agency or similar.
3. In order to be as open and transparent as
possible we
started a new blog
to warn people of the potential dangers and to update them of the
changes we made. We echoed this message on all our social media channels
(1,
2),
Facebook (1,
2),
Google+
and Reddit (1,
2) as well as emailing all our current and previous customers (in
case a previous customer renewed without being aware that they should
update).
1.
The website itself was not vulnerable at all, at any time. Our OpenVPN
servers though, were changed to a different version of OpenSSL that was
vulnerable on 2/27/2014. So, a vulnerability existed on our servers from
2/27/2014 through 4/8/2014, for a total of 39 days. We
replaced/regenerated the certs on all clients and servers, since they
were potentially exposed, within the day.
2. Small, but of course possible. We use
HMAC-based TLS authentication at both ends of the connection, using
separate halves of a shared key, as recommended by OpenVPN. This creates
a signature of each packet which is attached to the packet. The server
drops any packets that are unsigned or incorrectly signed. In the past,
this has primarily been used to prevent / slow down a DDoS attack, since
the attacker would need to securely hash each packet using the right
half of the shared key in the way that the OpenVPN client does.
Even with the suggestion from OpenVPN that
TLS auth could form a kind of protection against Heartbleed, it isn't
foolproof, given that we have to distribute the key with each client or
no one would be able to connect to our servers. As the researcher who
created the OpenVPN penetration test earlier this week noted, it
wouldn't be that difficult for a determined hacker to discover the TLS
auth key and modify his attack to use it. It does, however, prevent a
drive-by attack where we are hit more or less randomly as a VPN services
provider.
The worst case scenario is that someone
obtained our older server private key and was able to decrypt live data
and create a man-in-the-middle attack against our users during the 39
days we were using OpenVPN 2.3.2. Account credentials could have been
compromised, and the private key could have conceivably been as well.
Once we replaced OpenVPN to a non-vulnerable version and the server
certificate was replaced, that vector was closed.
3. We sent out an email notice to our
customers.
When
the Heartbleed announcement first broke, on the 7th April, we reviewed
our servers and customer portal system and found that they did not
utilize the affected OpenSSL versions.
When OpenVPN released their patch
to fix HeartBleed, we immediately implemented this in our own client and
released this on the 10th April 2014. Moving forward, our next client
release will use OpenVPN 2.3.3 which we hope to release in the coming
week.
We are also in the midst of an entire
customer portal revamp to improve security and usability which we hope
to release in a month or so and are considering a complete reissue of
all keys when this is released. The revamp was initiated many months ago
and was not as a result of the HeartBleed bug but is in line in our
continuing efforts to improve our system's security.
Our OpenVPN implementation implements
tls-auth with Perfect Forward Secrecy (PFS) would protect past
communications from retrospective decryption so the risk is mitigated.
In this scenario an attacker can not attack OpenVPN instances without
the TLS-auth key. Our customer portal processing system never used the
affected OpenSSL versions and remained with the older OpenSSL 0.9.8.
Users may request for a manual regeneration of their keys if they wish
to be overly cautious by opening a ticket with us.
We sent out an email announcement to all
users immediately, as well as a Facebook and
Blog post on the 8th April 2014 3.22 PM GMT+8. We then pushed an
update to our VPN clients on the 10th April with the patched OpenVPN
version as well.
1.
In a response to Heartbleed, NordVPN has changed private keys for all
servers. Also, the main NordVPN's certificate has been revoked and a new
one has been added. Our OpenSSL libraries have been upgraded from
version 1.0.1e to a safe 1.0.1g.
2. For users: potential user detail leaks
such as user names and passwords, but this is very unlikely as data that
malicious people could get was in random locations in a server memory
and user details are not kept in the memory for an entire session.
For servers: Private SSL certificate keys
are used to encrypt and decrypt data communications between user and a
VPN server. If anyone could have received a certificate and perform a
man in the middle attack, all data which was sent from a VPN server to
the user could have been decrypted.
3. The information was constantly shared to
our users via our live chat and e-mails. Also the pop-up, an
announcement line and the blog records were used to inform the steps we
were taking in a response to Heartbleed.
Here was the latest blog record
about Heartbleed:
https://nordvpn.com/blog/heartbleed-vulnerability-has-been-removed/
1.
When the Heartbleed security news broke, our engineering unit
immediately scanned all our servers and upgraded to latest version the
few servers (about 4% of our infrastructure) that were using vulnerable
versions of OpenSSL.
Our team then progressively patched absolutely all
our servers in an attempt to enjoy other bugfixes (unrelated to
security) accompanied with the successive new versions of OpenSSL.
Vulnerable servers were patched within less than one hour and the
non-vulnerable ones progressively got all upgraded within 24 hours.
We then researched about the implication of
this bug and with the security community, we came to the conclusion that
it was beyond reasonable doubt, even though most of our servers were
non-vulnerable, that a new re-generation of private keys was indeed
necessary. Indeed, extraction of private keys on vulnerable servers
proved possible.
Since re-generating complete new sets of
private and public keys undeniably involves a downtime and
reconfiguration on user end, we also took this opportunity' to
completely upgrade our encryption scheme, now leading the industry with CBC mode of AES with 256-bit as cipher, hash algorithm of 512-bit SHA
(SHA512) and control channel of 4096-bit RSA through TLSv1/SSLv3 and
with 256-bit AES, enforced to all customers by default.
The latest move does not necessarily respond
to Heartbleed, but at least it makes it 100% theoretically impossible
that the Heartbleed bug has any implication on the current VPN network,
as the latter is using not only new private and public keys, but also
completely new encryption algorithms.
2. It is very complex to answer with
certainty what truly happened. But basically, a hacker who knew about
this security hole before it went public (or within the few minutes
between the time the news broke and the time we patched vulnerability),
could have hacked the 4% of our servers infected with the vulnerable
version of OpenSSL. They could have retrieved our private keys, and thus
would potentially be able to decrypt the traffic that has been generated
by our services before they have been updated with new private keys.
Any service that did not either re-generated
new private keys (and offered new certificate files to customers) or
upgraded completely its encryption scheme (or optimally having done
both), is at risk of being exposed to full decryption because the keys
could have been stolen at anytime before the patch was enforced on
vulnerable servers, and vulnerability across any network of more than a
hundred servers built over the course of several months or years was
undeniably present at sporadic levels.
Now, factually, only a very close circle of
white hat hackers were aware of this security hole and exploiting it in
relation to keys vulnerability took us or anyone with security
experience several days to figure out (wisely we applied precautionary
principle and upgraded the keys well before). That means it would take
at least some hours for most experienced hackers to have been able to
exploit Heartbleed, hence the keys have had a thin chance of being
compromised since the vulnerable servers were patched few minutes after
0day news.
3. We offered a public blog article within
less than 24 hours after OpenSSL released new version and Heartbleed bug
came out to public. This article can be found
here and we explain in it that we successfully updated our OpenSSL
software to latest version, even though most of our servers were using
non-vulnerable versions of OpenSSL.
The upgrade itself started few
minutes after the security news broke.
Twenty four hours later, we
published another article to warn customers that we will be shutting
down the entire network for less than 5 minutes (with downtimes of few
seconds for each server) as we will be both re-generating new private
and public keys, as well as upgrading our cipher and authentification
encryption.
Seventy eight hours later, we published a
final article to explain that the upgrade has now been undertaken
and that all users should download again the new configuration and
certificate files in order to be able to connect to our network.
All these articles were advertised on our
Twitter account. Finally, we sent a mass e-mail (the first time in our
history) to all our customers to explain again to them that they should
download new configuration and certificate files, as well as preferably
change their passwords.
1.
We are using Ubuntu on all servers. We have updated all our 12.04 Ubuntu
versions next day, we are also using older Ubuntu where we use
unaffected OpenSSL version.
2. We think the only risk is that it was
possible to steal the username and passwords for the client area. We
think that getting these details from the memory would be very
complicated.
3. We
published an article here.
All
of the gateway servers were updated to a non-exploitable version of
OpenSSL as soon as we heard about the issue, within hours of the initial
public notice.
We do not believe any of our key information could have
been exploited in such a short amount of time, but we're still planning
to re-issue keys with the next client version, which should be updated
by this weekend. We are also issuing new .ovpn files on our website.
Once the updated client has been issued, we will be creating a blog post
informing our clients about the changes.fanon
1.
What steps has your company taken in response to Heartbleed (website,
servers etc)?
In summary, our website was running on an
older server with OpenSSL libraries that pre-dated the introduction of
the Heartbleed bug into OpenSSL, so we feel our customer confidential
information was not at risk due to Heartbleed. Among our VPN network
gateways, many were on a vulnerable version of OpenSSL or a vulnerable
build of OpenVPN server.
Those that were vulnerable were updated and
restarted within hours of the public announcement. Due to the short time
between public announcement and our updates, we feel the risk of key
disclosure was very small, but as a precaution the next release of
Octane OpenVPN client will update the client keys.
In addition, this vulnerability in a key
internet platform spurred us to consider a number of other scenarios
which has resulted in us adding some cool new features and options in
our OctaneVPN client which will be released soon.
2. Straight up, this was a serious bug in a
major internet platform. The risk and vulnerability is same for all
websites and services that relied on OpenSSL for encryption. In general,
based on research others have posted, it appears the worst case would be
that a private encryption key could be obtained by an untrusted third
party. In addition, it appears this would leave no traces.
Assuming others were not exploiting the
Heartbleed vulnerability before its public announcement, we feel the
risk of a private key release was very small due to the short time
window between public announcement and us applying patches to our
gateway servers. There is no evidence or unusual patterns that would
lead us to suspect our gateways were targeted. Our website was not
vulnerable to Heartbleed since it was running an older OpenSSL version
prior to when the Heartbleed bug first entered the OpenSSL code.
Remember, most sensitive web traffic is
already encrypted by the end website/browser via SSL before it is
encrypted again by a VPN network, so an attacker would need both a VPN
private key and also the end website's private key (say Amazon.com or
gmail.com keys) to even start to have a chance.
The possibility of
obtaining one key through Heartbleed is remote, but doing it for two
keys and the correct two keys for a given data packet before those sites
were patched or new keys issued is that much harder.
3. How we communicated the above to our
users.
a) We developed a
dedicated web page
b) We have worked with individual customers through our support channel
to answer specific questions
c) Our OctaneVPN client will notify customers automatically as new
releases are available
d) A comprehensive email will be pushed to customers once the new client
features are placed in production
1.
The Heartbleed bug potentially exposed data being passed over the
OpenSSL encryption protocol using TLS extension 15. IPVanish did not and
continues not to support the TLS extension 15, meaning all IPVanish
users were and are safe from this bug.
2. In addition to our point above, our
entire Network Operations team conducted a deep dive to verify and
confirm that no steps were needed in response to Heartbleed. We also
continue to monitor the situation and will take the necessary steps if
and when necessary.
3. We proactively communicated to our users
via our
homepage,
blog,
social media handles (including Twitter, Facebook and Google+), and
affiliate network, that all IPVanish users have been and continue to be
safe from Heartbleed.
We additionally notified users that even though IPVanish itself never had a breach of security, we recommend they update
their passwords if they use the same credentials across different
services.
1.
The first step was taken almost immediately. Our intrusion prevention
system was updated with the Heartbleed signature within 2 hours of the
announcement. We performed an audit and identified the vulnerable
systems. The last vulnerable VPN node was patched at 9:00 AM on
4/7/2014.
The affected servers had new keys created
from an unaffected CA. We used to use two CA's. 1 for our shared only
server clusters and the 2nd one for our shared, dynamic and modulating
server clusters. Our Shared IP CA had their certificates revoked and is
no longer used anywhere.
We already had a plan in progress to do an
overhaul of our OpenVPN configurations that will include a standardized
configuration across the three different VPN server builds we use. It
includes an update to our network security, lowers our key
re-negotiation time from 60 minutes to 30 minutes or less and uses a
dedicated offline server purchased recently to serve as our air-gapped
CA. When this rolls out we will issue new certificates across the
network for the final time.
Our webserver was patched later that
morning. We requested a new SSL certificate on 4/8/2014 and it was
applied on 4/9/2014. We use Viscosity by Sparklabs as our VPN client. As
soon as they released their OpenSSL patch it was pushed out to the
clients.
2. This was a major vulnerability. No matter
how much some providers downplayed it. For LiquidVPN an attacker could
have signed up to our service and got their hands on our shared TLS-Auth
key. With that in hand they could decipher portions of user VPN session
data but every 60 minutes keys are re-negotiated so their access would
be limited.
Website usernames and passwords could be
compromised. Users were susceptible to man in the middle attacks. VPN
usernames/passwords could be stolen.
3. We wanted to take a very proactive and
transparent approach to this problem. However we had to secure users
session data first. So we issued several updates beginning on April 7th.
There is a handful of twitter posts they can be found @liquidvpn.
Our basic announcements (there were several)
can be found
on the website. The
network status section has more information than the announcements.
Finally after everything was secured and our updates were complete we
published a
blog post.
As
soon as the vulnerability became known to us, between late night of
April the 7th and early morning of April the 8th in Italy, we
immediately started to get documentation.
We began to work on the system
minutes after we fully understood the problem and how the buffer
over-read could be provoked and exploited.
Luckily our setup which involves Perfect
Forward Secrecy both with OpenVPN and on the web server and the fact
that our VPN servers do not keep any database or other data pertaining
to users made the vulnerability not very risky for our VPN users.
Most of our VPN servers already were running
non-vulnerable OpenSSL branches, as well as the various backend servers
(a vital part of our infrastructure). On top of that VPN servers, web
server and clients never contact directly backend servers, so we found
ourselves in a very favorable situation. Our frontend web servers on the
contrary were vulnerable.
We proceeded to make sure that OpenSSL
version on the VPN servers was not vulnerable, patch OpenSSL in our web
sites and revoke the SSL certificate, reboot all the web servers to make
sure that no vulnerable in-memory OpenSSL was still loaded, install new
key and new SSL certificate on every frontend web server, change
internal use keys and certificates, change every administrative password
on every server, patch OpenSSL on the couple of VPN servers which ran
OpenSSL 1.0.1f and reboot them.
We performed attacks against all of our own
servers to make sure that the vulnerability was not there. For this we
must thank very much external, trusted reviewers who with dedication and
passion continuously search for vulnerabilities in our servers and
report to us the results - you know who you are, thanks again! All of
the above was completed between 11.00 AM and 11.00 PM April the 8th CEST.
However, we soon realized that we had to
keep into account that the vulnerability is client-side too, so the fact
that our servers were "secured" could not be considered sufficient.
Therefore we had to face the non-trivial problem to reach and inform our
users, which was solved with a "dramatic" decision about a radical
upgrade to the system which would have been performed after only a few
days.
The upgrade would have forced users to get
informed because from a certain point in time they could not connect
anymore to VPN servers until they upgraded.
Under a marketing point of
view it appeared as an extremely risky decision, but now that two weeks
have passed by we can say that this decision was wise, and anyway it was
the right thing to do regardless of any marketing consideration. And it
was also a good chance to switch to bigger keys and perform some radical
optimizations that we could not perform without disconnecting users for
several minutes.
About information to the public, we started
with a
public announcement on April the 8th, as soon as we had clear ideas
on what users needed to do. This was linked also through Twitter and
Facebook. The post was updated in real time while we were working on the
system.
The final steps were to renew the users
keys. We needed first to find an effective way to "encourage" users to
upgrade their systems.
We decided to switch to 4096 bit RSA and DH keys,
with new certificates, in a precise moment in the future (after just few
days), to maximize the probability that when a user was forced to
regenerate configurations, keys and certificates, he/she would have been
brought more easily to upgrade any possible vulnerable part of his/her
system. This was
announced here.
And we sent via PM and e-mail (to those
users who entered a valid e-mail address in their account data) a link
to the announcement. At the same time we powered up the customer service
for any clarification and to face any possible, massive wave of support
requests.
Since we do not outsource the customer service we did not need
to impart lessons to customer care personnel in order to make them
understand the problem, saving us many hours and allowing us to be
confident that customers were correctly supported in case of need.
Additionally we could count on our competent, supporting and very active
community in our forums.
1.
We have scanned all services and devices, our web servers and OpenVPN
server installations do not use the vulnerable version of OpenSSL
affected by Heartbleed.
The tools we used:
Manual checks were done on all other
equipment such as Cisco routers. We have opened a internal review on the
possibility of switching our SSL solution to PolarSSL.
2. Risk is only associated with users
sharing passwords between VPNsecure accounts on services that were
affected. We have advised users to change the password on the account
which automatically regenerates the openvpn keys.
3. Facebook notifications were sent out,
along with a news article and email.
1.
We've been very quick addressing the issue, and we started patching
everything immediately after the public vulnerability disclosure (Twitter
announcement).
- First we added a firewall rule to
temporarily block and log all Heartbleed probes against our servers,
allowing us to run the upgrades and issue new encryption keys while not
being exposed
- Website's SSL certificate has been changed and we asked the issuer of
the old certificate to revoke it; it was revoked one day later
- The upgrade process of all affected servers running the vulnerable
OpenSSL libraries was completed and all services restarted in the next
few hours
- After finishing the updates, we generated new encryption keys for our
OpenVPN service and pushed them on all servers
- Our Client Software has been updated on April 8 to include the
non-vulnerable OpenVPN binaries
2. We don't believe that the risks our users
faced were of high importance until then, but once the vulnerability
became public - taking all necessary measures to mitigate the risks and
protect our infrastructure was obviously the best thing a responsible
company would do.
3. We announced on Twitter minutes after the
vulnerability public disclosure that we're already updating the servers.
Once everything was secure on April 8, we issued a
detailed statement on our website and it was sent by email to all
our customers.
1.
Our servers operate under versions of Linux that were not affected by
this. Our OpenVPN servers use a custom build of OpenVPN that use non
affected versions of OpenSSL. We use TLS which also minimizes the risk
2. The risks were minimal, since on the
server side nothing was vulnerable.
3. Other than advising customers to upgrade
their OpenVPN there was nothing else to be done.
1.
Our experts evaluated possible risks, replaced the certificate and
published a blog post.
2. Fortunately we are not severely affected.
Possible men-in-the-middle attacks, the same as all other websites on
the web. VPN services are not affected and we could not expose any
private user information. More details are in the blog post.
3. We published a blog post, notified all
our followers in Facebook and Twitter, asking to change password for
other affected services. There is no need to change passwords for
Seed4.Me accounts.
