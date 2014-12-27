from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from models import parkingspot, parkingarea
from serializers import parkingspotserializer, parkingareaserializer

# Create your views here.
def index(request):
    return render(request, 'home.html', {})

# proxy service to workaround the CORS problem using gmaps directions api straight from javascript
def gmapsDirectionProxy(request, origin, destination):
    pass

class parkingspotviewset(viewsets.ModelViewSet):
    queryset = parkingspot.objects.all()
    serializer_class = parkingspotserializer

class parkingareaviewset(viewsets.ModelViewSet):
    queryset = parkingarea.objects.all()
    serializer_class = parkingareaserializer

