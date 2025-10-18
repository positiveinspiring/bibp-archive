# Evade Government Surveillance Stay Anonymous Online

> Source: https://www.bibliotecapleyades.net/SOCIOPOLITICA/sociopol_internet135.htm

by Chris Dougherty
January 3, 2013
from
VirtualThreat Website
Why stay anonymous online?
In todays society there are
people and automated devices that are recording your deepest, most
private thoughts and activities.
Each day we voluntarily divulge the most
intimate details of our lives through
social networking accounts,
email,
banking apps,
online games and more. In addition, governments and corporations can
censor and block our traffic based on whatever standards are in place that
day.
Government agencies, hackers and
sophisticated bot networks are capturing every piece of digital data
that we transmit through all of our Internet-connected gadgets. Smartphones,
Smart TVs, computers, tablets, and so much more
they are all vulnerable,
nothing is safe these days. Even your old clam-shell phone isnt safe.
This is because many phone providers route your
calls over media using the Internet Protocol at some point within their
network. For example, long distance providers transfer calls over VoIP all
the time.
Whether youre browsing the Web, signing up for a new online game, or simply
checking your email, you are constantly leaving tracks and giving away
information to anyone with access and the knowledge to analyze the traffic.
Once the data is compiled the attacker can build
an incredibly accurate profile of not only your online life but your
real-world life as well.
I know, most people say,
Why would hackers want to hack into my
life? I am not that important.
You have to understand that these intruders
into our lives are scanning huge blocks of Internet addresses at a time.
They dont care who you are. Your computer is simply another target IP
address as they scan through thousands of computers and devices in their
search for more information.
Once collected they take all the information and
funnel it into databases where they can search through it later for
high-valued loot.
Dont believe me? Just read the following story
about what our own government does:
The NSA
is Building The Countrys Biggest Spy Center - Watch What You Say - Big
Brother Goes Live September 2013.
So, the big question is, how can you stay anonymous online? Free from
government censorship and potential eavesdropping from some hacker or
three-letter government agency that wants to invade your privacy while you
use your computer.
In comes Whonix, the Anonymous Operating
System!
Use Whonix, The
Anonymous Operating System, Stay Anonymous Online
Whonix is a free, general purpose
computer operating system based on
Virtual Box, Linux and
Tor.
The purpose of Whonix is to allow Internet users
the ability to stay anonymous online. This is most beneficial to users in
regimes that
censor and
monitor access to the Internet, but it can also be used by anyone who
values their privacy, or doesnt want their activities tracked online.
By design, IP address leaks are meant to be impossible while using Whonix.
The developers claim even
malware with admin privileges cant find the Whonix Workstations real
IP address or location. This is because Whonix consists of two (virtual)
computers.
One machine acts as a gateway or router and runs
only Tor, a sophisticated
anonymity software. This machine is called the Whonix-Gateway.
The other machine, which called the Whonix-Workstation,
is on a completely isolated network that only allows Internet connections to
be routed through the Whonix-Gateway.
Tor, the technology on which Whonix is built, is a free software, along with
an open network consisting of thousands of computers located around the
world. Together they strive to provide anonymity for individuals accessing
the Internet. The Tor Project helps you defend against a form of network
surveillance, known as
traffic analysis, that threatens everyones personal freedom and
privacy.
Tor helps to reduce the risks of both simple and advanced traffic analysis
by distributing your Internet requests over several places on the Internet,
so no single point can link you to your destination.
The idea is similar to using a hard-to-follow
series of roads while driving in order to throw off somebody who is tailing
you.
Whonix automatically sets up an isolated network environment where your
virtual Workstation can perform all normal Internet related tasks such as
checking email, browsing web sites, blogging, connecting to corporate VPNs,
etc.
However all of that outbound traffic is then
routed in such a way that it can only pass through your virtual Gateway,
which encrypts the packets and sends them over several hops on the TOR
network prior to landing at their final destination.
How Whonix Works: Figure 1
Once your traffic leaves the Whonix Gateway it
is routed directly through the TOR network.
Instead of taking a direct route from source to
destination, data packets on the Tor network take a random path through
several relays, so no observer at any single point can tell where the data
came from or where its going.
The relays even take additional steps to erase
your tracks periodically along the way.
How Whonix Works: Figure 2
Routing Through TOR
In the event that the Workstation user initiates
a request to a new website or Internet resource, the Gateway simply selects
an alternate path through the TOR network as seen in Figure 3.
How Whonix Works: Figure 3
Using An Alternate TOR Path
There is a bit of a caveat to this system,
however.
As indicated by the red dotted-lines in the
images above, the last hop in the TOR network passes the traffic in the
clear to the final destination. One of the primary functions of this
computer, as an exit node, is to decrypt the data packets before they are
passed off to their final destination.
This means this exit node could be vulnerable to
a man-in-the-middle attack, or it could have even been placed there for the
specific purpose of monitoring exit traffic by a hacker or government
agency. While the exit node would still have no information regarding the IP
address or location of the original Workstation user, it would know the type
of Internet request that they sent to the destination server.
This scenario can be averted by using SSH tunnels or a VPN on top of the TOR
network.
One would only have to install the appropriate
software on the Whonix Workstation in order to provide an end-to-end
encryption solution for the traffic. Another method to bypass the
man-in-the-middle scenario would be to employ the use of TOR
Private
Bridges or
Private Exit Nodes.
It is important to note however that Whonix can be effectively used by most
people right out of the box for web browsing, blogging and private
conversations.
In order to make use of Whonix you will need to
download a free copy of VirtualBox.
Once VirtualBox has been downloaded and installed you can
download the Whonix-Workstation and the Whonix-Gateway packages from SourceForge.
Once downloaded, just import the machine files into VirtualBox as-is and
start them up, you dont need to change any settings
also be sure to start
the Whonix-Gateway machine before firing up the Workstation image.
The default login credentials for both virtual machines are as follows:
====================
Username: user
Password: changeme
Username: root
Password: changeme
====================
Once the images have completed the boot process you can login and run the
whonixcheck command from the CLI (command line interface) in order to
verify proper connectivity to the TOR network.
The Workstation output should
look similar to the following :
How Whonix Works: Figure 4
Workstation output
from the whonixcheck command
Be sure to watch for my article in the
next few days detailing step-by-step instructions on how to install
VirtualBox and Whonix on your computer. Let me know what you think of this
anonymity solution in the comments below
UPDATE: 01/09/2013
The Whonix development team forwarded the
following important information about the anonymity provided from their
product and Tor:
Whonix Statement
