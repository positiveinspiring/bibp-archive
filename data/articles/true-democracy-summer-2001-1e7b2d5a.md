# TRUE DEMOCRACY SUMMER 2001

> Source: https://www.bibliotecapleyades.net/SOCIOPOLITICA/shadow/s37.htm

Idaho National Engineering Laboratories
(INEL)
http://http://www.robotics.com/robomenu/inel.html
ASA, in association with Inuktun Services, has recently designed, fabricated and delivered the above project IN ONLY 19 WEEKS. The system includes a tethered articulated duct/pipe robot and surface control system. The robot incorporates three short segments which enables travel around 90 degree bends in 8"=20 circular ducts. The control station gives the operator high resolution images from the robot's cameras and provides two joysticks for control of the robot's 4 tracks. Overlaid on the camera images are displays from the various system sensors. The Scope of Work included all design, assembly, testing, delivery and training.
The ROBOT is comprised of:
The FRONT SEGMENT consists of:
Two tracks, an electronics can and a camera pan and tilt unit.
Incorporated into these units are:
- a forward facing high definition camera,
- a lighting system, a solid state gyroscope,
- a radiation sensor (hard beta and gamma) and
- a sampling arm for taking specimens.
The MIDDLE SEGMENT houses the main vehicle microprocessor, telemetry electronics and robot tip & tilt sensors.
The REAR SEGMENT consists of: Two tracks, a power conditioning system, a rear facing camera, rear facing lights and the tether connection.
The CONTROL STATION incorporates:
An OPERATOR DISPLAY, which shows various information including;
- the selected camera view
- the Vehicle segment positions
- the camera pan and tilt orientation
- the Vehicle tip, tilt and direction
- an artificial horizon
- the temperature of internal components
All displays and associated icons can be turned off, minimized or moved on the screen.
The OPERATOR CONTROLS, which include;
- separate joysticks for the front and rear tracks
- emergency on/off switch
- camera select switch
- pan and tilt controls
- light intensity switches for all three sets of lights
- cruise control on/off switch
- slave rear tracks to front tracks on/off switch
The MAIN CONTROL COMPUTER is a VME based system utilizing a 68000 series processor and associated I/O and interface cards. All control programs in the Control Station are Written in "C" using VxWorks, a real time Operating System. The vehicle microprocessors are written in a combination of C and assembly language.
In April of 1995 ASA was awarded a contract by INEL (Idaho National Engineering Laboratory) to upgrade their Duct Inspection Robot's Electronics. This system was originally designed and built jointly by ASA and Inuktun. INEL required the electronics package inside the Duct Inspection Robot to be revised to achieve two major goals; to be easily expandable in the future and to control a new device that INEL had designed. This device mechanically changes the angle of the Robot's tracks so as to accommodate the different diameters of pipe encountered while navigating the Duct system. Previously the tracks were held at fixed angles by replaceable brackets.
The new electronics package contains 8 networked microprocessors communicating over the I=B2C bus. These are configured as one master processor and seven slave processors. The microprocessor selected for this purpose was the PIC16c73 just released by Microchip. The rear segment contains the master processor, which exchanges RS485 commands from, and status information to, the supervisor over the tether. The master then communicates this information to/from the appropriate slaves. A slave microprocessor located in each of the four tracks provides PWM control of the track's motor and provides temperature feedback. The center segment of the robot's body contains two more slave processors. One is responsible for changing the angle of the tracks and reading various feedback devices such as the roll and pitch sensors. The other integrates the rate gyro signal providing direction of travel information and counts pulses from the radiation sensor. The final slave processor is located in the front 'camera' can and is responsible for the panning and tilting of the camera head, the motion of the manipulator arm, the camera's iris control and pan/tilt feedback information.
Each slave processor on the I=B2C bus has a unique 'address' which the master processor uses to communicate with it. New devices can be easily added to the system by suitably programming a PIC16c73 or related processor, giving it an as yet unused address and plugging it into one to the spare communications ports on the exterior of the robot. The master software would then be slightly modified to talk to the new device. Apart from the design and assembly of the new device, only minor software changes need to be made in order to accommodate it.
- System Concept and Design for all robot electronics and entire Control Station.
- System Mechanical, Electrical and Software Engineering for above.
- Fabrication Supervision and Assembly.
- System Testing and Site Installation.
Project Completed : 1994 & 1995(Control Upgrade)
To view ASA's Web Page for this project (and other ASA custom automation projects) go to: http://asa.bc.ca/asa/projs/inel.html
To view the Web Page for this project produced by INEL go to: http://http://www.inel.gov/.robotics/10.html
Send inquiries to the address below:
gsedun@asa.bc.ca (Garry Sedun, President)
Or phone us at (604)-656-2002 (Canada) and ask for Garry Sedun
