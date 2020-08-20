# reaktor-fall-2020
On a Debian and Ubuntu systems, there is a file called /var/lib/dpkg/status that holds information about software packages that the system knows about. Write a small program in a programming language of your choice that exposes some key information about packages in the file via an HTML interface.

### Introduction
This is my solution for Reaktors pre-assigment for junior positions. The application lists packages from /var/lib/dpkg/status file via HTML interface and user can easily view more information about individual packages by clicking the name. If application is unable to open the status file, it will open a file with mock data to let users of different systems to test the interface. I took this as an excellent opportunity to use and learn more about a programming language that I have not used before in a "larger" scale.
