<h1>UVSIM Application</h1>
The UVSIM application is a graphical user interface (GUI) designed to assist computer science students to learn machine language and computer architecture. 

The UVUSIM is a virtual machine and can only interpret a machine language called BasicML. 
The UVSim contains CPU, register, and main memory. An accumulator – a register into which information is put before the UVSim uses it in calculations or examines it in various ways. All the information in the UVSim is handled in terms of words.

A word is a signed four-digit or a six-digit decimal number, such as +1234, -5678 or +001234, -005678. The BasicML program must be loaded into the main memory starting at location 00 before executing. Each instruction written in BasicML occupies one word of the UVSim memory (instruction are signed four-digit or six-digit decimal number). Each location in the UVSim memory may contain an instruction, a data value used by a program or an unused area of memory. The first two digits of each BasicML instruction are the operation code specifying the operation to be performed.

<h2>Features</h2>
<li><strong>GUI Interface:</strong> A user interface for interacting with the application.</li>
<li><strong>File Import:</strong> Within the User Interface, open files and edit.</li>
<li><strong>Multi File:</strong> This application supports multiple files to execute.</li>
<li><strong>Multi word flexibility:</strong> Select from four-digit or six-digit words memory will seamlessly be edited for user.</li>

<h2>Installation and Setup</h2>
<li><strong>For Install:</strong></li> As this is a GitHub repository, to access the program the user will need to clone the repository. 
<li><strong>For Setup:</strong></li> Once the repository has been cloned and is found within local computer files. Please note that PIP install files may be necessariy to run the program successfully. These include: PySide6 

<h2>Contributing</h2>
This program was implemented for educational purposes. Many Design patterns learned throughout the course have been applied however not all were beneficial for the use of this program and therefore were not implemented.

<h2>Limitations</h2>
This program is a designed to aid students in learning machine language. While the program does allow four or six- digit words please note that both cannot be accomidated within the same file. This application is not suitible for commercial use or deployment.
