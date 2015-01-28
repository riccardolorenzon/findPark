from django.db import models
from django.contrib.auth.models import User
import datetime

# represents a delimited area of the city/town
class parkingarea(models.Model):
    code = models.CharField(max_length=255)
    description = models.TextField()

# represents the class of the transport vehicle(a bike parking spot occupies less space than a car parking spot)
class transportclass(models.Model):
    code = models.CharField(max_length=255)
    description = models.TextField()

# represents a parking spot on the state <state> starting from <laststatechange>
class parkingspot(models.Model):
    status = models.CharField(max_length=255)
    laststatechange = models.DateTimeField(blank = True, null = True)
    #spot localization
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    #parking area
    area = models.ForeignKey(parkingarea, null=True, blank=True, default = None)
    #transport type
    transportcode = models.CharField(max_length=255, blank = True)
    #fields to avoid collisions between concurrent users
    creation_user = models.ForeignKey(User, related_name="creations_user", default=None)
    creation_datetime = models.DateTimeField(auto_now=False, auto_now_add=True, default=datetime.datetime.now())
    last_modified_user = models.ForeignKey(User, related_name="last_modified_user", default=None)
    last_modified_datetime = models.DateTimeField(auto_now=True, auto_now_add=True, default=datetime.datetime.now())

# represents the parking spot history, one object is created for each parking vehicle
class parkingspothistory(models.Model):
    state = models.CharField(max_length=255)
    ready = models.DateTimeField()
    occupied = models.DateTimeField()
    #spot localization
    latitude = models.DecimalField(max_digits=18, decimal_places=8)
    longitude = models.DecimalField(max_digits=18, decimal_places=8)
    #parking area
    area = models.ForeignKey(parkingarea)
    #transport type
    transportcode = models.CharField(max_length=255)

# represent the driver user
class appuser(models.Model):
    code = models.CharField(max_length=255)
    parkingspots = models.ManyToManyField(parkingspot, through='Parking', blank=True)
    transportclasses = models.ManyToManyField(transportclass, through='Driving', blank=True)
    #current localization
    latitude =  models.DecimalField(max_digits=18, decimal_places=8)
    longitude =  models.DecimalField(max_digits=18, decimal_places=8)

# represents a passenger
class passenger(models.Model):
    code = models.CharField(max_length=255)
    models.ForeignKey(appuser)

class Parking(models.Model):
    appuserfield = models.ForeignKey(appuser)
    parkingspotfield = models.ForeignKey(parkingspot)

class Driving(models.Model):
    appuserfield = models.ForeignKey(appuser)
    transportclassfield = models.ForeignKey(transportclass)







