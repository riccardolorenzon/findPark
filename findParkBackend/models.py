from django.db import models

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
    laststatechange = models.DateTimeField()
    #spot localization
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    #parking area
    area = models.ForeignKey(parkingarea)
    #transport type
    transportcode = models.CharField(max_length=255)

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

# represent the driver user, this entity
class appuser(models.Model):
    code = models.CharField(max_length=255)
    models.ManyToManyField(parkingspot, blank=True)
    models.ManyToManyField(transportclass, blank=True)
    #current localization
    latitude =  models.DecimalField(max_digits=18, decimal_places=8)
    longitude =  models.DecimalField(max_digits=18, decimal_places=8)

# represents a passenger
class passenger(models.Model):
    code = models.CharField(max_length=255)
    models.ForeignKey(appuser)






