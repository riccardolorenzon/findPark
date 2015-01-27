from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from models import parkingspot, parkingarea, appuser
from serializers import parkingspotserializer, parkingareaserializer, appuserserializer
import urllib2
import json
from rest_framework import permissions
from rest_framework import status

# Create your views here.
def index(request):
    return render(request, 'home.html', {})

# proxy service to workaround the CORS problem using gmaps directions api straight from javascript
def gmapsDirectionProxy(request, origin, destination):
    OVER_QUERY_LIMIT = True
    url = "http://maps.googleapis.com/maps/api/directions/json?origin=" + origin + "&destination=" + destination + "&sensor=false"
    response = urllib2.urlopen(url)
    return HttpResponse(response, content_type='application/json')

class parkingspotviewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = parkingspot.objects.all()
    serializer_class = parkingspotserializer
    def create(self, request):
        """
            Overrides the create method in order to get
            extra params: the id of the created object.
            When this is done, we pass the method to his parent.
        """
        serializer = parkingspotserializer(data= request.data)
        if serializer.is_valid():
            parking_spot = serializer.create(serializer.validated_data)
            parking_spot.save()
            return HttpResponse(json.dumps({'id' : parking_spot.id}),
                            status=status.HTTP_201_CREATED, content_type="application/json")
        else:
            return HttpResponse(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


class parkingareaviewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = parkingarea.objects.all()
    serializer_class = parkingareaserializer

class appuserviewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = appuser.objects.all()
    serializer_class = appuserserializer



