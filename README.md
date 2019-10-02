# A simple docker database made with python flask

## Setup
Build the dockerdb, to build the dockerdb make sure you are in directory by default "dockerdb" then run: $ docker build -t dockerdb .

Start the dockerdb: $ docker run -p 80:5000 dockerdb

Start the dockerdb on the background: $ docker run -d -p 80:5000 dockerdb

## Stop
To stop the dockerdb: docker stop "CONTAINER ID"

## Send data
To send data in the dockerdb you can do it by either using the gui in the webbrowser or by using the commandline

Send data by using commandline: $ curl -X PUT http://127.0.0.1:80/ -d DATA="typedatahere"

Send data by using browser: navigate to http://127.0.0.1:80/ then make sure "Media type" is on "application/x-www-form-urlencoded" then type "DATA=typedatahere"

## Get data
To get data from dockerdb: $ curl -X GET http://127.0.0.1:80/
