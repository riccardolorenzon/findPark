__author__ = 'riccardo'

# unit tests class writtent for REST APIs
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class ParkingSpotsTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('parkingspot-list')
        response = self.client.post(url, {'status': 'open',
                    'latitude': '0.000',
                    'longitude': '1.000', 'area': None }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)