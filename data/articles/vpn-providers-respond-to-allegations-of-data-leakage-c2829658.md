# VPN Providers Respond to Allegations of Data Leakage

> Source: https://www.bibliotecapleyades.net/SOCIOPOLITICA/sociopol_internet210.htm

A team of researchers from
universities in London and Rome have published a paper in which
they claim that many of the world's top
VPN providers leak IPv6
traffic.
TorrentFreak has spoken to several
companies highlighted in the report and today we publish their
responses.
As Internet users seek to bypass
censorship, boost privacy and achieve a level of anonymity, VPN
services have stepped in with commercial solutions to assist
with these aims. The uptake among consumers has been impressive.
Reviews of VPN services are
commonplace and usually base their ratings on price and speed.
At TorrentFreak we examine many
services annually, but with a focus on privacy issues
instead.
Now a team of researchers from
universities in London and Rome have published a paper titled
'A Glance through the VPN Looking Glass
- IPv6 Leakage and DNS
Hijacking in Commercial VPN clients' after investigating 14 popular services on the market today.
"Our findings confirm the
criticality of the current situation: many of these providers
leak all, or a critical part of the user traffic in mildly
adversarial environments.
The reasons for these failings are
diverse, not least the poorly defined, poorly explored nature of VPN usage, requirements and threat models," the researchers
write.
While noting that all providers are
able to successfully send data through an encrypted tunnel, the
paper claims that problems arise during the second stage of the
VPN client's operation: traffic redirection.
"The problem stems from the fact
that
routing tables are a resource that is concurrently managed
by the operating system, which is unaware of the security
requirements of the VPN client," the researchers write.
This means that changes to the
routing table (whether they are malicious or accidental) could
result in traffic circumventing the VPN tunnel and leaking to
other interfaces.
IPv6 VPN
Traffic Leakage
"The vulnerability is driven by
the fact that, whereas all VPN clients manipulate the IPv4
routing table, they tend to ignore the IPv6 routing table.
No rules are added to redirect IPv6 traffic into the tunnel.
This can result in all IPv6 traffic bypassing the VPN's
virtual interface," the researchers explain.
As illustrated by the chart above,
the paper claims that all desktop clients (except for those
provided by Private Internet Access, Mullvad and VyprVPN) leaked
"the entirety" of IPv6 traffic, while all providers except Astrill were vulnerable to IPv6 DNS hijacking attacks.
The paper was covered yesterday by
The Register with the scary-sounding title
"VPNs are so insecure you might as well wear a KICK ME sign" but without
any input from the providers in question.
We decided to contact
a few of them for their take on the paper.
PureVPN told TF that
they,
"take the security of our
customers very seriously and thus, a dedicated team has been
assigned to look into the matter."
Other providers had already received
advanced notice of the paper.
"At least for AirVPN the paper
is outdated,"
AirVPN told
TorrentFreak.
"We think that the researchers,
who kindly sent the paper to us many months in advance and
were warned about that, had no time to fix [the paper]
before publication. There is nothing to worry about for AirVPN."
"Current topology allows us to
have the same IP address for VPN DNS server and VPN gateway,
solving the vulnerability at its roots, months before the
publication of the paper."
TorGuard also knew of
the whitepaper and have been working to address the issues it
raises.
The company adds that while The
Register's "the sky is falling" coverage of yesterday is "deceptive", the study does illustrate the need for providers to
stay vigilant.
Specifically, TorGuard says that it
has launched a new IPv6 leak prevention feature on Windows, Mac
and Linux.
"Today we have released a new
feature that will address this issue by giving users the
option of capturing ALL IPv6 traffic and forcing it through
the OpenVPN tunnel.
During our testing this method
proved highly effective in blocking potential IPv6 leaks,
even in circumstances when these services were active or in
use on the client's machine," the company reports.
On the DNS hijacking issue, TorGuard
provides the following detail.
"It is important to note that
the potential for this exploit only exists (in theory) if
you are connected to a compromised WiFi network in which the
attacker has gained full control of the router. If that is
the case, DNS hijacking is only the beginning of one's
worries," TorGuard notes.
"During our own testing of TorGuard's OpenVPN
app, we were unable to reproduce this when using private DNS
servers because any DNS queries can only be accessed from
within the tunnel itself."
Noting that they released IPv6 Leak
Protection in October 2013, leading VPN provider
Private
Internet Access told TorrentFreak that they feel the paper
is lacking.
"While the article purported to
be an unbiased and intricate look into the security offered
by consumer VPN services, it was greatly flawed since the
inputs or observations made by the researchers were
inaccurate," PIA said.
"While a scientific theory or
scientific test can be proven by a logical formula or
algorithm, if the observed or collected data is incorrect,
the conclusion will be in error as well."
PIA criticizes the report on a
number of fronts, including incorrect claims about its DNS
resolver.
"Contrary to the report, we have
our own private DNS daemon running on the Choopa network.
Additionally, the DNS server that is reported, while it is a
real DNS resolver, is not the actual DNS that your system
will use when connected to the VPN," the company explains.
"Your DNS requests are handled
by a local DNS resolver running on the VPN gateway you are
connected to. This can be easily verified through a site
like
ipleak.net.
Additionally
we do not allow our DNS
servers to report IPv6 (AAAA records) results. We're very
serious about security and privacy."
Finally, in a comprehensive response
(now
published here) in which it notes that its Windows client is
safe, PIA commends the researchers for documenting the DNS
hijacking method but criticizes how it was presented to the VPN
community.
"The DNS Hijacking that the
author describes [..] is something that has recently been
brought to light by these researchers and we commend them on
their discovery.
Proper reporting routines would
have been great, however. Shamefully, this is improper
security disclosure," PIA adds.
While non-IPv6 users have nothing to
fear, all users looking for a simple fix can disable IPv6 by
following instructions for
Windows,
Linux
and
Mac.
