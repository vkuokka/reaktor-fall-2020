# reaktor-fall-2020
On a Debian and Ubuntu systems, there is a file called /var/lib/dpkg/status that holds information about software packages that the system knows about. Write a small program in a programming language of your choice that exposes some key information about packages in the file via an HTML interface.

## Introduction
This is my solution for Reaktor's pre-assigment for junior positions. The application lists packages from /var/lib/dpkg/status file via HTML interface and user can easily view more information about individual packages by clicking the name. If application is unable to open the status file, it will open a file containing mock data to let users of different systems to test the interface. I took this as an excellent opportunity to use and learn more about a programming language that I have not used before in a larger scale before.

#### Website demo
Application demo can be found from https://reaktorfall-app.herokuapp.com/.

## Getting started

#### Prerequisites
You need to have python3 installed into your computer. You can find installation guides for different operating systems here: https://realpython.com/installing-python/

#### Installation
Clone the repository and install required package distributions with the following commands:
```
git clone https://github.com/vkuokka/reaktor-fall-2020.git && cd reaktor-fall-2020 && pip3 install -r requirements.txt
```
#### Running the application
After succesful installation you can run the application with the following command:
```
python3 wsgi.py
```
If the launch is succesful, similiar text should appear into terminal window:
```
 * Serving Flask app "app.main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Notice the last row. Opening the URL with your browser of choice will display the HTML interface.
