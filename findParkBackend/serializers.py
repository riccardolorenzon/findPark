__author__ = 'riccardo'
from django.forms import widgets
from rest_framework import serializers
from models import parkingspot, parkingarea, transportclass

class parkingspotserializer(serializers.HyperlinkedModelSerializer):
    area = serializers.HyperlinkedRelatedField(queryset = parkingarea.objects.all(), view_name='area-detail', format='json')
    class Meta:
        model = parkingspot
        fields = ('state', 'laststatechange', 'latitude', 'longitude', 'area', 'transportcode')

class parkingareaserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = parkingarea
        fields = ('code', 'description')

