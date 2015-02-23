findPark
========
FindPark is a web application that trace people's parking spots around the world. 
The aim is to provide a simple way for drivers to find the nearest parking spot. 

FindPark back end is made on the Python/Django stack. 
FindPark front end is made using HTML5, CSS3, Twitter Bootstrap and AngularJS. 

FindPark is deployed(Beta) on Heroku.
```
REST api:

POST api-auth/                            : user authentication

GET api/parkingspots/                     : get parking spots(pagination is equal to 10)
POST api/parkingspots/                    : insert new parking spot
GET api/parkingspots/(?P<pk>[0-9]+)/      : retrieve the parking spot identified by pk
PUT api/parkingspots/(?P<pk>[0-9]+)/      : update all fields of the parking spot identified by pk
PATCH api/parkingspots/(?P<pk>[0-9]+)/    : update only provided fields of the parking spot identified by pk
DELETE api/parkingspots/(?P<pk>[0-9]+)/   : delete the parking spot identified by pk

GET api/parkingareas/                     : get parking areas(pagination is equal to 10)
GET api/parkingareas/(?P<pk>[0-9]+)/      : retrieve the parking area identified by pk
PUT api/parkingareas/(?P<pk>[0-9]+)/      : update all fields of the parking area identified by pk
PATCH api/parkingareas/(?P<pk>[0-9]+)/    : update only provided fields of the parking area identified by pk
DELETE api/parkingareas/(?P<pk>[0-9]+)/   : delete the parking area identified by pk
```
