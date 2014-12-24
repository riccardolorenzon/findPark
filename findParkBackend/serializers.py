__author__ = 'riccardo'
from django.forms import widgets
from rest_framework import serializers
from models import parkingspot, parkingarea, transportclass

class parkingspotserializer(serializers.HyperlinkedModelSerializer):
    area = serializers.HyperlinkedRelatedField(queryset = parkingarea.objects.all(), view_name='parkingarea-detail', format='json')
    def validate_status(self, value):
        """
        Check that the blog post is about Django.
        """
        if value.lower() not in ['open', 'closed']:
            raise serializers.ValidationError("error on status value: <possible choices are: open, closed> ")
        return value
    class Meta:
        model = parkingspot
        fields = ('status', 'laststatechange', 'latitude', 'longitude', 'area', 'transportcode')


class parkingareaserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = parkingarea
        fields = ('code', 'description')

