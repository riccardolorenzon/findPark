__author__ = 'riccardo'

# unit tests class writtent for REST APIs
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class ParkingSpotsTests(APITestCase):
    def test_create_parkingspot(self):
        """
        ensure you can create a new parking spot and add it to the parking spot list via rest
        """
        url = reverse('parkingspot-list')
        response = self.client.post(url, {'status': 'open',
                    'latitude': '0.000',
                    'longitude': '1.000', 'area': None }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_update_parkingspot(self):
        """
        ensure you can update the status of an existing parking spot via rest
        """
        url = reverse('parkingspot-detail')
        response = self.client.put(url, {''

        }, format = 'json')
        self.assertEqual(1 == 1)

