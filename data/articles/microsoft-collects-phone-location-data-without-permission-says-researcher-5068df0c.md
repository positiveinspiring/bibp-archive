# Microsoft Collects Phone Location Data Without Permission - Says 
Researcher

> Source: https://www.bibliotecapleyades.net/SOCIOPOLITICA/sociopol_win-micro-gates09.htm

by Declan McCullagh
September 1, 2011
from
News.CNet Website
A security researcher says that Microsoft's
Windows Phone 7
software can transmit your location without your explicit
permission.
An analysis by Samy Kamkar says that the Camera application sends the
device's location - complete with latitude and longitude, a unique ID, and
nearby Wi-Fi access points - to Microsoft even when the user has not given
the app permission to do so.
Here are
more details on how it works.
"The Windows Mobile operating system is
clearly sending information that can lead to accurate location
information of the mobile device regardless of whether the user allowed
it," Kamkar wrote in an analysis made public yesterday as part of a
lawsuit filed against Microsoft.
Lawyers for the suit, who are seeking class
action status, hired him to perform the testing.
Excerpt from analysis by Samy
Kamkar,
which he says shows the
Camera app transmitting
the phone's latitude and
longitude to Microsoft servers.
Microsoft declined to comment to CNET.
Kamkar, who once landed in legal hot water for creating a worm that garnered
him a million friends on MySpace overnight in 2005, has recently focused on
geolocation privacy issues, including
creating a Web site that allowed
people to look up the unique ID of their computer or Wi-Fi access point and
see its location.
Google
disabled that service after a CNET
article in June drew attention to privacy concerns.
The privacy issue that Kamkar identified may not be huge:
-
For one thing,
there's no evidence even a single customer was harmed as a result
-
Second,
turning off location services completely (through the phone's global
settings option) should disable any transmission of geolocation data to
Microsoft
Like Google, Apple, and Skyhook Wireless,
Microsoft is assembling
a crowd-sourced database using what customers' phones can see.
On the other hand, if he's right, Microsoft would be violating its own
privacy pledges to customers.
A
Microsoft Web page says the company "surveys available Wi-Fi access
points" only when "the user has allowed a particular application to access
location services and the application requests location information."
Microsoft has made similar statements to Congress.
Kamkar says the Camera application transmits location data to Microsoft's
inference.location.live.net even if the user chooses to say "no" when
prompted.
Concern this year over geolocation privacy began in April, when researchers
showed that iPhones and iPads surreptitiously record their owner's
approximate location and store the data on the device.
Apple responded by calling it a "bug" and
promising a fix (see
related articles.)
The Seattle-based law firm Tousley Brain Stephens, which boasts of
having "a national reputation for achieving exceptional results" in class
action lawsuits, filed the case against Microsoft yesterday in federal
district court in Washington state.
Their complaint, which cites an August 1 CNET article, says,
"Microsoft surreptitiously forces even
unwilling users into its non-stop geo-tracking program in the interest
of developing its digital marketing grid."
(There's no evidence, however, that Microsoft is
using its geolocation database for marketing. These databases are typically
used to speed up location fixes with Wi-Fi when cellular connectivity is
poor.)
The class action lawyers claim that Microsoft violated a federal law called,
-
the Stored Communications Act
-
the Electronic Communications Privacy
Act
-
the Washington Consumer Protection Act
Additional Information
Microsoft Curbs Wi-Fi Location Database
by Declan McCullagh
August 1, 2011
from
News.CNet Website
Microsoft's Live.com database
showed an HTC mobile device
moving across Columbus, Ohio,
last week.
(Credit: Screen snapshot by Declan McCullagh/CNET)
Microsoft has ceased publishing the estimated
locations of millions of laptops, cell phones, and other devices with Wi-Fi
connections around the world after a
CNET article on Friday highlighted
privacy concerns.
The decision to rework Live.com's geolocation
service comes following scrutiny of the way Microsoft made available its
database assembled by both
Windows Phone 7 phones and what the company
calls "managed driving" by Street View-like vehicles that record Wi-Fi
signals accessible from public roads.
Every Wi-Fi device has a unique ID, sometimes
called a MAC address, that cannot normally be changed.
Live.com's database, which published the precise geographical locations of
Wi-Fi devices, was working normally last Friday. By Saturday morning,
Elie
Bursztein, a postdoctoral researcher at the Stanford Security Laboratory who
had
analyzed the Live.com service, noticed that access had been restricted.
Stanford researcher Elie Bursztein had suggested that Microsoft
should curb access to its database.
Stanford researcher Elie
Bursztein
had suggested that Microsoft
should curb access to its database.
That follows a similar move by Google, which
curbed access to its location database days after a
June 15 CNET article
appeared. Skyhook Wireless, which provides similar location services,
already used a limited form of geolocation to protect privacy.
The two companies' moves to limit access to their databases come as
concerns
about location privacy have grown. Apple came under fire in April for
recording logs of approximate location data on iPhones, and it eventually
released a fix.
That controversy sparked a series of disclosures
about other companies' location privacy practices,
questions and
complaints
from congressmen, a pair of U.S. Senate hearings, and the now-inevitable
lawsuits
seeking class action status.
Reid Kuhn, a Microsoft program manager on
the Windows Phone engineering team, confirmed the change in a statement sent
to CNET today:
This change adds improved filtering to
validate each request so that the service will no longer return an
inferred position when a single Media Access Control address is
submitted.
While it was not possible to use the service
to track a roaming mobile phone or laptop using its MAC address prior to
this change, Microsoft is keenly aware of the sensitivity around all
privacy issues, especially those surrounding geolocation...
Microsoft's commitment to privacy means that not only will we seek to
build privacy into products, but we'll also engage with key stakeholders
in government, industry, academia, and public-interest groups to develop
more effective privacy and data protection measures.
We will continue to update our service with
improvements that benefit the consumer in both positioning accuracy as
well as individual privacy.
But Kuhn's statement doesn't appear to be true.
One example: CNET tracked an HTC mobile device
with the Wi-Fi MAC Address of 7C:61:93:33:44:65 moving from a home on
Meadowlawn Drive in Columbus, Ohio, last Tuesday to an address on East
Mithoff Street last Wednesday.
A Microsoft representative did not have an immediate response.
Microsoft has declined repeated requests from CNET to respond to a list of
questions, including whether the database includes only Wi-Fi devices acting
as access points, or whether client devices using the networks have been
swept in as well - something that Google did using Street View.
A
May blog post touts "Transparency About
Microsoft's Practices," but it doesn't provide details.
If Microsoft collects and publishes only the Wi-Fi addresses of access
points, the privacy concerns are lessened. But hundreds of millions of
phones and computers are used as access points - tethering is one example,
and the feature is built into OS X - meaning that their locations could be
monitored.
It's true that Wi-Fi addresses, or MAC addresses, aren't typically
transmitted over the Internet. But anyone within Wi-Fi range can record
yours, and it's easy to narrow down which addresses correspond to which
manufacturer.
Someone, such as a suspicious spouse, who can navigate to the About screen
on an iPhone or a laptop's configuration menu can
obtain it in a few seconds
as well. And hobbyist hacker Samy Kamkar
created a proof-of-concept
code last year that uses what's known as a cross-site scripting attack to
grab the location of Wi-Fi routers that can be seen from an unsuspecting
visitor's computer.
Microsoft's database extends beyond U.S. locations. A CNET test last week
showed that Live.com returned locations linked to street addresses in,
-
Leon,
Spain
-
Westminster, London
-
a suburb of Tokyo, Japan
-
Cologne, Germany
Update, 9:20 a.m. PT Tuesday
