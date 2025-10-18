# Detect Computer and Email Monitoring

> Source: https://www.bibliotecapleyades.net/SOCIOPOLITICA/sociopol_internet141.htm

August 7, 2011
from
HighTech-Edge Website
How to check if
someone is monitoring your computer and email
In the world of IT, its quite common for large corporations, offices and
call centers to set up some kind of monitoring software to track each
employers computer sessions, and on a more creative but sinister level, its
also quite common for such software to be put to criminal use.
Falling victim to computer spying technology, which can be used to obtain
passwords from key strokes, as well as other personal data stored on your
machine or in the cloud, is no joke; an estimated 10 million people fall
victim to identity theft every year, and the Internet, as well as other home
or office networks are increasingly becoming prime targets when it comes to
extracting such data.
Windows XP, Vista and
Windows 7 all feature whats known as the
built-in "Remote Desktop."
This allows another user on the same network to
connect directly to your machine. Thankfully this feature is no threat when
it comes to spying on your session as the Remote Desktop on a workstation
will only allow one user at a time to use the desktop. [Microsoft Windows
Answers]
Plus, Windows also informs the user every time someone wishes to connect to
their computer, so theres little chance of your session being monitored in
this way.
Note:
There is a hack for this, but in most cases
you wont have to worry. Youve never really 100% safe when
browsing a network, even super encrypted networks can be hacked.
If government corporations and IT giants
such as SONY (eh hmm) have troubles, the average home user stands no
chance if they were to come under direct attack from an expert hacker.
Basically, what this boils down to is that anyone wanting to anonymously
connect to your machine will need third party software, which is way easier
to detect.
Programs used to spy on computer are typically
known as remote control software or virtual network computing (VNC)
software.
If you suspect theres a similar type of software running on your machine,
there are few ways you can check if someone is monitoring your session.
How To Detect If Your
Computer Is Being Monitored
First you can simply check the programs installed on your machine.
Many IT technicians assume people wont be savvy
enough to look for these pieces of software, so theres a chance you could
find them openly installed on machines linked up to office, call center and
corporate networks.
Most of these pieces of software also install an icon in the task bar, so
when its running you might be able to locate it by hovering and clicking on
the appropriate icon.
Detect Computer and
Email Monitoring
Check the task bar for VNC Monitoring Software
If you dont see anything in the task bar, then head to:
Start > All Programs, and check the list of
programs.
Alternatively you can go to:
My Computer > C: drive > Program Files.
From here you can view the folders each program
has created upon installation.
Theres a very good chance youll come across some applications youve never
heard of. If thats the case, a quick Google search will tell you exactly
what the piece of software does.
Similarly, you can check your Windows processes in the Task Manager for
diagnosis.
Here youll be able to view all the processes
running at any one time on your machine.
Press Ctrl + Alt + Del to open the Task
Manager.
The first thing you should do is scan the details in the User Name column.
You should only see your User Name, Local Service, Network Service, and
System. If anything else is listed here, it means someone is watching your
session.
Next you can check through your processes.
Some, such as WINWORD.EXE (Microsoft Word), will
be easy enough to identify, but youll no doubt have to run a quick Google
search to find out what others, such as the ATKOSD.EXE (an audio driver for
XP), do.
Again, youre looking for anything that could resemble a piece of remote
control software, for example WINVNC.EXE.
There could be any amount from 36-50 processes running on a typical machine
(depending of course, on how many programs are installed on the computer) so
be prepared for lots of searches the first time you do this.
Should you find such software; with administrative rights youll be able to
easily uninstall the program by heading to:
My Computer > Add/Remove Programs.
However, if someone went to trouble of
installing software to monitor your session, youd like to think theyd have
the intelligence to try and cover up their spying - and it is possible to
install such a program and hide it from the view of your average computer
user.
So if youve searched through all your computer programs and find nothing,
yet you still suspect that someone is watching your every move, then the
next port of call (excuse the lame geek pun) would be to check your
computers communication ports.
Any data shared with your computer - packets transferred to and from the
Internet or any other network - must be sent and received on these ports.
Windows Firewall works by blocking certain ports to protect your machine.
Third party spying apps work by hijacking and transferring data through one
of these ports. Thankfully its possible to check and configure which ports
are being used, and what programs have access to them.
To modify the programs allowed to access the Internet, head to:
Control Panel > Windows Firewall.
Navigate to the tab labeled Exceptions.
Modify Programs Allowed To
Access The Internet
Here youll be able to view which programs have
access to a network and on what port they are doing so.
First off, scroll down the list and check for any programs that could be
VNC or remote control related. If youre not sure what the programs are,
again a quick Google search will tell you exactly what youre looking at.
Should you locate any software, as long as youre logged in as
administrator, you should have no problem, removing it in the same manner
already mentioned:
My Computer > Add/Remove Programs >
Uninstall specific program.
How to Detect If Your
Email Is Being Monitoring
To monitor emails in a similar fashion, POP and SMTP are configured to send
and receive emails on the networks servers, where they can also be stored
and viewed later.
If you use email regularly at work, theres a good chance your account is
being monitored. And if you use an email client such as Outlook or
Thunderbird, its actually very easy for company to set up monitoring for
your email.
Thankfully its also just as easy to find out if your email is being
monitored in such a way, however its not always a good idea to alter these
settings, companys put them there for a reason and trying to bypass them
can sometimes cost you your job, and can even result in legal action being
taken against you.
For that reason never modify your works
computer network settings, and always use your personal email with caution
when at work. However if you want to be sure that your email is being
monitored:
In Outlook (Thunderbird will be similar) go to:
Tools > Email Accounts > Properties.
Check the values of your for POP and SMTP
server. If your email is being monitored it will be directed to networks
server, where all emails can be recorded and viewed.
How To Detect If Your
Web Browsing Experience Is Being Monitored
To monitor web browsing experiences without third party software, a network
must employ whats known as a proxy server to intercept the data. The proxy
server acts a bridge where data is first sent. Here it can be modified,
saved, or even denied from being transferred to another server.
To check if your computer is connected to a proxy server go to:
[Internet Explorer] Tools > Internet Options
> Connections > LAN Settings.
[Firefox] Tools > Options > Advanced > Network > Connections > Settings.
If youre going through a proxy, the Proxy
Server box will be checked.
There will also be an assigned I.P. address and
a port number.
How to Close Firewall Resources
Source
