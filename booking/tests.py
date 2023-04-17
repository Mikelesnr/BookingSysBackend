from django.test import TestCase
from .common import open_seats, check_capacity, count_booked
from .models import Booking
from driver.models import Driver

# Create your tests here.


class TestBookings(TestCase):
    def setUp(self):
        bookings = [
            {
                "client_name": "Skylar",
                "client_surname": "Lawson",
                "bus_reg": "ACD 654321",
                "trip_time": "1pm",
                "trip_date": "07/04/2023",
                "ticket_id": "a23",
                "trip_depature": "Town",
                "trip_destination": "Highlands"
            },
            {
                "client_name": "darrel",
                "client_surname": "Adams",
                "bus_reg": "ACD 654321",
                "trip_time": "1pm",
                "trip_date": "07/04/2023",
                "ticket_id": "a23",
                "trip_depature": "Town",
                "trip_destination": "Highlands"
            },
            {
                "client_name": "sky",
                "client_surname": "Adams",
                "bus_reg": "ACD 654321",
                "trip_time": "1pm",
                "trip_date": "07/04/2023",
                "ticket_id": "a23",
                "trip_depature": "Town",
                "trip_destination": "Highlands"
            },
            {
                "client_name": "james",
                "client_surname": "Bean",
                "bus_reg": "ACD 654321",
                "trip_time": "1pm",
                "trip_date": "07/04/2023",
                "ticket_id": "a23",
                "trip_depature": "Town",
                "trip_destination": "Highlands"
            },
            {
                "client_name": "jim",
                "client_surname": "Dugen",
                "bus_reg": "ACD 654321",
                "trip_time": "1pm",
                "trip_date": "07/04/2023",
                "ticket_id": "a23",
                "trip_depature": "Town",
                "trip_destination": "Highlands"
            },
            {
                "client_name": "chifiwa",
                "client_surname": "Xhosa",
                "bus_reg": "ACD 654321",
                "trip_time": "1pm",
                "trip_date": "07/04/2023",
                "ticket_id": "a23",
                "trip_depature": "Town",
                "trip_destination": "Highlands"
            }
        ]
        bus = {
            "id": 3,
            "name": "Billy",
            "surname": "James",
            "bus_reg": "ACB 197374",
            "no_of_seats": "72",
            "bus_type": "Big bus",
            "route": "Borowdale - Town"
        }

        def test_check_capacity(self):
            self.assertEqual(check_capacity(bus.get('bus_reg')), "72")
