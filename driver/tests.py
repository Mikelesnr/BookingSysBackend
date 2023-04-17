from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status


class DriverListTestCase(APITestCase):

    def test_driver_list_get(self):
        response = self.client.get(reverse('drivers'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
