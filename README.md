# A simple docker database made with python flask

## Setup
Build the dockerdb, to build the dockerdb make sure you are in the right directory by default "dockerdb"

    Build the dockerdb: $ docker build -t dockerdb .

    Start the dockerdb: $ docker run -p 80:5000 dockerdb

    Start the dockerdb in the background: $ docker run -d -p 80:5000 dockerdb

## Stop
    To stop the dockerdb: $ docker stop "CONTAINER ID"

## Send data
To send data in the dockerdb can be done by either using the gui in the webbrowser or by using the commandline

    Send data by using the commandline: $ curl -X PUT http://127.0.0.1:80/ -d DATA="DATA GOES HERE"

Send data by using browser: navigate to http://127.0.0.1:80/ type your data and click on submit.

## Get data
    To get data from dockerdb using the command line: $ curl -X GET http://127.0.0.1:80/db/

To getdata from dockerdb using the browser navigate to http://127.0.0.1:80/db/
