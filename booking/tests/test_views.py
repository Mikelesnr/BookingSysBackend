from django.test import TestCase, Client
from django.urls import reverse
from booking.models import Booking, Trip
import json


class TestViews(TestCase):

    def test_booking_GET(self):
        client = Client()

        response = client.get(reverse('booking'))

        self.assertEqual(response.status_code, 200)

    def test_buses_GET(self):
        client = Client()

        response = client.get(reverse('buses'))

        self.assertEqual(response.status_code, 200)

    def test_bookind_GET(self):
        client = Client()

        response = client.get(reverse('trips'))

        self.assertEqual(response.status_code, 200)
