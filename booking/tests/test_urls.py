from django.test import SimpleTestCase
from django.urls import reverse, resolve
from booking.views import (booking, booking_edit,
                           buses, trip, seats_available, trips, trip_edit)


class TestUrls(SimpleTestCase):

    def test_booking_is_resolved(self):
        url = reverse('booking')
        print(resolve(url))
        self.assertEquals(resolve(url).func, booking)

    def test_buses_is_resolved(self):
        url = reverse('buses')
        print(resolve(url))
        self.assertEquals(resolve(url).func, buses)

    def test_trip_is_resolved(self):
        url = reverse('trip')
        print(resolve(url))
        self.assertEquals(resolve(url).func, trip)

    def test_seats_is_resolved(self):
        url = reverse('seats')
        print(resolve(url))
        self.assertEquals(resolve(url).func, seats_available)

    def test_trips_is_resolved(self):
        url = reverse('trips')
        print(resolve(url))
        self.assertEquals(resolve(url).func, trips)

    # def test_booking_manage_is_resolved(self):
    #     url = reverse('booking_manage')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func, booking_edit)

    # def test_trip_manage_is_resolved(self):
    #     url = reverse('trip_manage')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func, trip_edit)
