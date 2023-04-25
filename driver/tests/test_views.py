from django.test import TestCase, Client
from django.urls import reverse
from driver.models import Driver
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.drivers_url = reverse('drivers')
        self.driver_url = reverse('driver', kwargs={'id': '1'})

    def test_drivers_GET(self):

        response = self.client.get(self.drivers_url)

        self.assertEqual(response.status_code, 200)

    def test_diver_GET(self):
        bol = False
        response = self.client.get(self.driver_url)

        self.assertEqual(response.status_code, 200)
