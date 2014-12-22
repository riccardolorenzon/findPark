from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
def index(request):
    return HttpResponse('ciao a tutti')

class parkingspotviewset(viewsets.ModelViewSet):
    pass

class areaviewset(viewsets.ModelViewSet):
    pass