__author__ = 'riccardo'
from django.forms import widgets
from rest_framework import serializers
from models import parkingspot, parkingarea

class parkingspotserializer(serializers.HyperlinkedModelSerializer):
    area = serializers.HyperlinkedRelatedField(read_only = True, view_name='area-detail', format='json')
    transportcode = serializers.HyperlinkedRelatedField(read_only = True, view_name='transportcode-detail', format='json')
    class Meta:
        model = parkingspot
        fields = ('state', 'laststatechange', 'latitude', 'longitude', 'area', 'transportcode')

class parkingareaserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = parkingarea
        fields = ('code', 'description')

