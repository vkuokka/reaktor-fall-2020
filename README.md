# reaktor-fall-2020
On a Debian and Ubuntu systems, there is a file called /var/lib/dpkg/status that holds information about software packages that the system knows about. Write a small program in a programming language of your choice that exposes some key information about packages in the file via an HTML interface.

### Introduction
This is my solution for Reaktors pre-assigment for junior positions. The application lists packages from /var/lib/dpkg/status file via HTML interface and user can easily view more information about individual packages by clicking the name. If application is unable to open the status file, it will open a file with mock data to let users of different systems to test the interface. I took this as an excellent opportunity to use and learn more about a programming language that I have not used before in a "larger" scale.

### Requirements and running the application
You will need to have python 3 installed to be able to run the application. After cloning this project run the following command inside the repository to install required distributions.
```
$> pip3 install -r requirements.txt
```
After successful installation of required distributions you should be able to run the application with the following command.
```
$> python3 wsgi.py 
 * Serving Flask app "app.main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
As you can see from the example, you should be able to start using the application by entering http://127.0.0.1:5000/ into your browsers searchbar. You can also view the application in action by heading to https://reaktorfall-app.herokuapp.com/. This address displays status.real file found in this repository as mentioned in the introduction.
