from django.contrib.gis.db import models

# represents a parking spot on the state <state> starting from <laststatechange>
class parkingspot(models.Model):
    state = models.CharField(max_length=255)
    laststatechange = models.DateTimeField()
    #spot localization
    poly = models.PolygonField()
    objects = models.GeoManager()
    #parking area
    area = models.ForeignKey(parkingarea)
    #transport type
    transportcode = models.ForeignKey(transportclass)

# represents the parking spot history, one object is created for each parking vehicle
class parkingspot(models.Model):
    state = models.CharField(max_length=255)
    ready = models.DateTimeField()
    occupied = models.DateTimeField()
    #spot localization
    poly = models.PolygonField()
    objects = models.GeoManager()
    #parking area
    area = models.ForeignKey(parkingarea)
    #transport type
    transportcode = models.ForeignKey(transportclass)

# represents a delimited area of the city/town
class parkingarea(models.Model):
    code = models.CharField(max_length=255)
    description = models.TextField()

# represents the class of the transport vehicle(a bike parking spot occupies less space than a car parking spot)
class transportclass(models.Model):
    code = models.CharField(max_length=255)
    description = models.TextField()

# represent the driver user, this entity
class appuser(models.Mode):
    code = models.CharField(max_length=255)
    models.ManyToManyField(parkingspot, blank=True)
    models.ManyToManyField(transportclass, blank=True)
    #current localization
    poly = models.PolygonField()
    objects = models.GeoManager()

# represents a passenger
class passenger(models.Model):
    code = models.CharField(max_length=255)
    models.ForeignKey(appuser)

