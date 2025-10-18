# Google Spans Entire Planet With GPS-Powered Database

> Source: https://www.bibliotecapleyades.net/SOCIOPOLITICA/sociopol_internetgoogle25.htm

by Cade Metz
September 19, 2012
from
Wired Website
Three years ago, a top Google engineer named
Vijay Gill was asked what he would do if someone gave him a magic wand.
At the time, Gill helped run the massive network
of data centers that underpins Googles online empire, and he was sitting on
stage at a conference in downtown San Francisco, discussing the unique
challenges facing this globe-spanning operation.
Jonathan Heilger - the man
who oversaw Facebooks data centers - sat a few seats away, and it was
Heiliger who asked Gill what he would add to Googles data centers
if he had a magic wand.
Gill hesitated before answering. And when he did
answer, he was coy. But he seemed to say he would use that magic wand to
build a single system that could automatically and instantly juggle
information across all of Googles data centers.
Then he indicated
that Google had already built one.
How do you manage the system and
optimize it on a global level? he said. That is the interesting part.
The conventional wisdom is that time
synchronization like that, on a global scale, that is accurate enough
for such a big distributed database... just isnt practical.
Andy Gross
It was little more than a teaser.
But about four
months later, Google dropped another hint. At a symposium in the mountains
of Montana,
Jeff Dean - one of Googles most important engineers - revealed that the
web giant was working on something
called
Spanner, describing it as a storage
and computation system that spans all our data centers.
He said the
plan was to eventually juggle data across as many as 10 million servers
sitting in hundreds to thousands of data centers across the globe.
The scope of the project was mind-boggling. But
Dean provided few details, and it wasnt clear whether Google was actually
using the platform in its live data centers. Then, on Tuesday, the paper hit
the web.
This week, as reported by
GigaOm and
ZDnet, Google published a
research paper detailing the ins and outs of
Spanner.
According to
Google, its the first database that can quickly store and retrieve
information across a worldwide network of data centers while keeping that
information consistent - meaning all users see the same collection of
information at all times - and its been driving the companys ad system and
various other web services for years.
Spanner borrows techniques from some of the
other massive software platforms Google built for its data centers, but at
its heart is something completely new.
Spanner plugs into a network of
servers equipped with super-precise atomic clocks or GPS antennas akin to
the one in your smartphone, using these time keepers to more accurately
synchronize the distribution of data across such a vast network.
Thats
right, Google attaches GPS antennas and honest-to-goodness atomic clocks to
its servers.
Its a big deal - and its really novel, says
Andy Gross, the principal architect of
Basho,
an outfit that builds an open source database called Riak that runs across
thousands of servers - though not nearly as many as Spanner.
The
conventional wisdom - at least among people with modest resources - is that
time synchronization like that, on a global scale, that is accurate enough
for such a big distributed database... just isnt practical.
Spanner may seem like an extreme undertaking,
and certainly, it tackles an unusual problem.
Few other companies on Earth
are forced to deal with so much data so quickly. But Googles massive data
center creations have a way of trickling down to the rest of the tech world.
The prime example is
Hadoop, a widely used number-crunching platform that
mimics technologies originally built at Google, and this trend will
likely continue.
If you want to know what the large-scale,
high-performance data processing infrastructure of the future looks like, my
advice would be to read the Google research papers that are coming out right
now, Mike Olson, the CEO of Hadoop specialist Cloudera,
said at recent event in Silicon Valley.
According to Charles Zedlewski,
vice president of products at Cloudera,
the company was already aware of Spanner - after recruiting some ex-Google
engineers - and it may eventually incorporate ideas from the paper into its
software.
Facebook is already
building a system thats somewhat similar to Spanner, in that it aims to
juggle information across multiple data centers. Judging from our
discussions with Facebook about this system - known as Prism - its quite
different from Googles creation.
But it shows that other outfits are now
staring down many of the same data problems Google first faced in years
past.
Jeff Dean and Sanjay
Ghemawat,
two of the most important engineers behind the Googlenet.
Image: Wired/Ariel Zambelich
Googles Bigger Table
The Spanner paper lists many authors, but two
stand out: Jeff Dean and Sanjay Ghemawat.
After joining Google from the
research operation at DEC - the bygone computer giant -
Dean and Ghemawat helped design three massive software platforms that
would have a major impact on the rest of the internet.
MapReduce and the
Google File System gave rise to Hadoop, while BigTable helped spawn an army
of NoSQL databases suited to storing and retrieving vast amounts of
information.
Spanner draws on BigTable, but it goes much
further. Whereas BigTable is best used to store information across thousands
of servers in a single data center, Spanner expands this idea to millions of
servers and multiple data centers.
The genius of the platform lies in something
Google calls the TrueTime API.
API is short for application programming
interface, but in this case, Google is referring to a central data feed that
its servers plug into. Basically, TrueTime uses those GPS antennas and
atomic clocks to get Googles entire network running in lock step.
A GPS
antenna taps into the Global Position System, which relies on a series of
space satellites to track time and location, while an atomic clock uses the
properties of individual atoms to maintain correct time.
One aspect of our design stands out: The
linchpin of Spanners feature set is TrueTime.
Google
Google declined to discuss Spanner.
The paper
speaks for itself, said a company spokeswoman.
But she did point to a
particular portion of the paper that highlights the importance of the API.
One aspect of our design stands out, the paper reads. The linchpin of
Spanners feature set is TrueTime.
To understand TrueTime, you have to understand
the limits of existing databases.
Today, there are many databases designed
to store data across thousands of servers. Most were inspired either by
Googles BigTable database or a similar storage system built by Amazon known
as Dynamo. They work well enough, but they arent designed to juggle
information across multiple data centers - at least not in a way that keeps
the information consistent at all times.
According to Andy Gross - the principal
architect at Basho, whose Riak database is based on Amazon Dynamo - the
problem is that servers must constantly communicate to ensure they correctly
store and retrieve data, and all this back-and-forth ends up bogging down
the system if you spread it across multiple geographic locations.
You have
to a do a whole lot of communication to decide the correct order for all the
transactions, Gross says, and the latencies you get are typically
prohibitive for a fast database.
Max Schireson - the CEO of 10gen, whose MongoDB
database follows in the footsteps of BigTable - puts it a different way.
Imagine, Schireson says, that youre using a web service to transfer money
between two bank accounts, one in Europe and another in Asia. If youre in
Europe, it may look like the transfer is complete. But to someone in Asia,
it might not, because theres a delay in communication.
There may even be cases, he says, where one
observer sees the money in both accounts at the same time. In short, the
service may not always work as advertised because not everyone has the same
view of the data. The data isnt consistent.
If you then consider a service used by millions
of people, you can see how large this problem can be.
If you have large
numbers of people accessing large numbers of systems that a globally
distributed so that the delay in communications between them is relatively
long, it becomes very hard to keep everything synchronized, he says.
If
you increase those factors, it gets even harder.
With TrueTime, Spanner solves this problem,
taking an approach that no one expected.
How to Keep TrueTime
Rather than try to improve the communication
between servers, Google spreads clocks across its network.
It equips various
master servers with GPS antennas or atomic clocks, and - working in tandem
with the TrueTime APIs - these time keepers keep the entire network in sync.
Or thereabouts.
A lot of current research [outside of Google]
focuses on complicated coordination protocols between machines
but this
takes a completely different approach, Gross says.
By using highly
accurate clocks and a very clever time API, Spanner allows server nodes to
coordinate without a whole lot of communication.
Just having a peek into the way Google does
this
is very valuable.
Andy Gross
In short, the TrueTime API taps into those
master time keepers, and servers across the network tap into the API.
TrueTime then tells the servers how much uncertainty there is over the
current time, and they can adjust their reads and writes accordingly.
Ordinary servers
tap into public atomic clocks in an effort to maintain the correct time.
But this method isnt as accurate as it could be, says Gross. Google has
gone a step further, installing its own atomic clocks - and GPS antennas -
directly on its machines.
The system was first used to help serve ads
across the Google empire, but it has seen expanded to all sorts of other
Google services.
The system also helps Google replicate and move data across
its network, and this helps the company accommodate data center repairs and
upgrades and even ride out network problems. When he first alluded to
Spanner three years ago, Vijay Gill talked of Google automatically moving
vast amounts of data out of facility that needed to be temporarily shutdown
because the temperature was too high.
The rub is that you cant use Spanner unless you
add hardware to your servers. In its paper, Google says the atomic clocks
arent expensive, and 10gens Max Schireson can see other outfits installing
similar equipment. But both Bashos Gross and Clouderas Zedlewski believe
the cost would be prohibitive for general use.
Gross says that building a system that relies on
such equipment doesnt make sense for an outfit like Basho. And Zedlewski
says much the same thing about Cloudera.
But even they see the future in
Spanner.
Like so many other NoSQL outfits, Basho aims to
serve large web players and other outfits facing epic amounts of online
data, and Gross says the fundamental ideas behind Spanner can help the
company do that.
Google tends to be ahead of the open source
state-of-the-art. Everyone cant afford atomic clocks, but we can learn from
the methods they use, he says. Just having a peek into the way Google does
this
is very valuable.
