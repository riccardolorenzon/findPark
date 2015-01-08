from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from models import parkingspot, parkingarea
from serializers import parkingspotserializer, parkingareaserializer
import urllib2
import json
from rest_framework import permissions

# Create your views here.
def index(request):
    return render(request, 'home.html', {})

# proxy service to workaround the CORS problem using gmaps directions api straight from javascript
def gmapsDirectionProxy(request, origin, destination):
    url = "http://maps.googleapis.com/maps/api/directions/json?origin=" + origin + "&destination=" + destination + "&sensor=false"
    response = urllib2.urlopen(url)
    return HttpResponse(response, content_type='application/json')

class parkingspotviewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = parkingspot.objects.all()
    serializer_class = parkingspotserializer

class parkingareaviewset(viewsets.ModelViewSet):
    queryset = parkingarea.objects.all()
    serializer_class = parkingareaserializer

