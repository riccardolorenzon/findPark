from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from models import parkingspot, parkingarea
from serializers import parkingspotserializer, parkingareaserializer

# Create your views here.
def index(request):
    return HttpResponse('home page')

class parkingspotviewset(viewsets.ModelViewSet):
    queryset = parkingspot.objects.all()
    serializer_class = parkingspotserializer

class parkingareaviewset(viewsets.ModelViewSet):
    queryset = parkingarea.objects.all()
    serializer_class = parkingareaserializer
