from driver.serializers import BusSerializer
from driver.models import Driver
from .serializers import BookingSerializer
from .models import Booking
from uuid import uuid4 as id
import json

# create objects and functions for booking functionality here


def check_capacity(reg):
    buses = Driver.objects.all()
    for bus in buses:
        if reg == bus.bus_reg:
            return bus.no_of_seats


def count_booked(reg, time):
    booked_seats = 0
    bookings = Booking.objects.all()
    for booking in bookings:
        if reg == booking.bus_reg and time == booking.trip_time:
            booked_seats += 1
    return booked_seats


def open_seats(reg, time):
    return int(check_capacity(reg)) - int(count_booked(reg, time))

def add_ticket_id(request):
    my_request = request.POST.copy()
    my_request['ticket_id'] = str(id())
    my_request = json.dumps(my_request)
    my_request = json.loads(my_request)
    return my_request



