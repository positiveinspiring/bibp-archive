# Skype With Care - Microsoft is Reading Everything You Write

> Source: https://www.bibliotecapleyades.net/SOCIOPOLITICA/sociopol_internet144.htm

Anyone who uses Skype
has consented to the company reading everything they write.
The H's associates in Germany at
heise Security have now
discovered that the Microsoft subsidiary does in fact make use of this
privilege in practice. Shortly after sending HTTPS URLs over the instant
messaging service, those URLs receive an unannounced visit from
Microsoft HQ in Redmond.
A reader informed heise Security that he had
observed some unusual network traffic following a Skype instant
messaging conversation. The server indicated a potential replay attack.
It turned out that an IP address which traced back to Microsoft had
accessed the HTTPS URLs previously transmitted over Skype.
Heise
Security then reproduced the events by sending two test HTTPS URLs, one
containing login information and one pointing to a private cloud-based
file-sharing service.
A few hours after their Skype messages, they
observed the following in the server log:
65.52.100.214 - - [30/Apr/2013:19:28:32 +0200]
"HEAD /.../login.html?user=tbtest&password=geheim HTTP/1.1"
The access is coming from systems which clearly
belong to Microsoft.
Source:
Utrace
They too had received visits to each of the
HTTPS URLs transmitted over Skype from an IP address registered to
Microsoft in Redmond.
URLs pointing to encrypted web pages frequently
contain unique session data or other confidential information. HTTP
URLs, by contrast, were not accessed. In visiting these pages, Microsoft
made use of both the login information and the specially created URL for
a private cloud-based file-sharing service.
In response to an enquiry from heise Security,
Skype referred them to a passage from its
data protection policy:
"Skype may use automated scanning within
Instant Messages and SMS to (a) identify suspected spam and/or (b)
identify URLs that have been previously flagged as spam, fraud, or
phishing links."
A spokesman for the company confirmed that
it scans messages to filter out spam and phishing websites.
This
explanation does not appear to fit the facts, however. Spam and phishing
sites are not usually found on HTTPS pages. By contrast, Skype leaves
the more commonly affected HTTP URLs, containing no information on
ownership, untouched.
Skype also sends
head requests which merely fetches administrative information
relating to the server. To check a site for spam or phishing, Skype
would need to examine its content.
Back in January, civil rights groups sent
an open letter to Microsoft questioning the security of Skype
communication since the takeover.
The groups behind the letter, which
included the
Electronic
Frontier Foundation and
Reporters
without Borders expressed concern that the restructuring resulting
from the takeover meant that Skype would have to comply with US laws on
eavesdropping and would therefore have to permit government agencies
and secret services to access Skype communications.
In summary, The H and
heise Security
believe that, having consented to Microsoft using all data transmitted
over the service pretty much however it likes, all Skype users should
assume that this will actually happen and that the company is not going
to reveal what exactly it gets up to with this data.
Think Your Skype Messages Get...
End-to-End Encryption?
Think Again...
by Dan Goodin
May 20 2013
from
ArsTechnica Website
Ars catches Microsoft
accessing links we sent in our test
messages.
If you think the private messages you send
over Skype are protected by end-to-end encryption, think again.
The Microsoft-owned service regularly scans
message contents for signs of fraud, and company managers may log the
results indefinitely, Ars has confirmed. And this can only happen if
Microsoft can convert the messages into human-readable form at will.
With the help of independent privacy and
security researcher
Ashkan Soltani, Ars used Skype to
send four Web links that were created solely for purposes of this
article.
Two of them were never clicked on, but the other two - one
beginning in HTTP link and the other HTTPS - were accessed by a machine
at 65.52.100.214, an
IP
address belonging to Microsoft.
For those interested in the technical
details, the log line looked like this:
'65.52.100.214 - - [16/May/2013 11:30:10] "HEAD /index.html?test_never_clicked HTTP/1.1" 200 -'
The results - which were similar but not
identical to those reported last
week by The H Security - prove conclusively that Microsoft
not only has ability to peer at the plaintext sent from one Skype user
to another, but that the company regularly flexes that monitoring
muscle.
In one sense, this shouldn't come as news.
Skype's privacy policy clearly states that it may (emphasis
added)
use automated scanning within Instant Messages and SMS to identify
spam and links to sites engaged in phishing and other forms of fraud.
And as Ars reported last year, since Skype
was acquired by Microsoft, the network running the service has been
drastically overhauled from its design of the preceding decade.
Gone are the peer-to-peer "supernodes" made
up of users with sufficient amounts of bandwidth and processing power;
in their place are some 10,000 Linux machines hosted by Microsoft. In
short, the decentralization that had been one of Skype's hallmarks was
replaced with a much more centralized network.
It stands to reason that messages traveling
over centralized networks may be easier to monitor.
Perception, meet reality
Still, there's a widely held belief - even
among security professionals, journalists, and human rights activists -
that Skype somehow offers end-to-end encryption, meaning communications
are encrypted by one user, transmitted over the wire, and then decrypted
only when they reach the other party and are fully under that party's
control.
This is clearly not the case if Microsoft
has the ability to read URLs transmitted back and forth.
"The problem right now is that there's a
mismatch between the privacy people expect and what Microsoft is
actually delivering," Matt Green, a professor specializing in
encryption at Johns Hopkins University, told Ars.
"Even if Microsoft is only scanning
links for 'good' purposes, say detecting malicious URLs, this
indicates that they can intercept some of your text messages. And
that means they could potentially intercept a lot more of them."
Specifics of the Microsoft scanning remain
unclear; one possibility is that the scanning and spam-checking happen
on Microsoft servers as communications pass through supernodes.
Another possibility is that the Skype client
on each end-user machine uses "regular expression" programming
techniques built into the software and sends only the links to Microsoft
servers.
"Either way, the finding does confirm
that somewhere along the stream, Microsoft/Skype has the ability to
intercept/extract content from your communications though we can't
conclusively say where," Soltani wrote in an e-mail to Ars.
"For example, even if the scanning was
happening client side, it's plausible that MS could be compelled to
push a ruleset to the Skype client that just logs/transmits all our
activity (similar to what
CarrierIQ was doing on the HTC phones)."
Helping to feed this confusion about exactly
what measures are taken to protect Skype messages is Microsoft's
management, which remains vague about the precise type of encryption its
service uses.
Asked for comment on this story, a
spokeswoman offered a statement that was identical to a single sentence
in the privacy policy. The statement didn't address my other question
that's equally important: does Microsoft record the links and other
content sent over Skype?
Eventually I found the answer, and
unfortunately it gives Microsoft all the wiggle room it needs.
It
states:
"Skype will retain your information for
as long as is necessary to:
(1) fulfill any of the Purposes (as
defined in article 2 of this Privacy Policy)
(2) comply with applicable
legislation, regulatory requests and relevant orders from
competent courts"
To be fair, Microsoft's scanning of Skype
messages isn't too different from
techniques Facebook
reportedly employs, and what any number of other online services do,
too.
As Green notes, these companies have a duty
to make sure their services aren't abused to circulate malware.
What's different in the case of Skype is the
misunderstanding among many users that links and other content sent over
the service are private. This misunderstanding is all the more
unfortunate given the possibility that this information plucked out of
private messages could be logged and retained for as long as some
nameless, faceless Microsoft manager deems appropriate.
Add to that the fact that a server bearing a
Microsoft IP address very well may click on any link you send over Skype
and it may not be such a good option for dissidents trying to lay low.
So the next time you use Skype, enjoy the
clarity of the voice communications, its generally slick user interface,
and its many other benefits. Just don't think the service can't peer
into your messages and store indefinitely what Microsoft managers want.
It can, and until officials specifically
disclose their practices, users should assume it does.
