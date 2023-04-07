from driver.serializers import BusSerializer
from driver.models import Driver
from .serializers import BookingSerializer
from .models import Booking
from uuid import uuid4 as id
import json

# create objects and functions for booking functionality here


def check_capacity(reg):
    '''
    checks the capcity of the bus using bus_reg number
    '''
    buses = Driver.objects.all()
    for bus in buses:
        if reg == bus.bus_reg:
            return bus.no_of_seats


def count_booked(reg, time):
    '''
    checks number of booked seats on the trip using bus_reg number and trip_time
    '''
    booked_seats = 0
    bookings = Booking.objects.all()
    for booking in bookings:
        if reg == booking.bus_reg and time == booking.trip_time:
            booked_seats += 1
    return booked_seats


def open_seats(reg, time):
    '''
    checks how many seats are available on the trip
    '''
    return int(check_capacity(reg)) - int(count_booked(reg, time))


def add_ticket_id(request):
    '''
    adds unique ticket id to request using uuid4 class
    '''
    my_request = request.POST.copy()
    my_request['ticket_id'] = str(id())
    my_request = json.dumps(my_request)
    my_request = json.loads(my_request)
    return my_request


def trip_creator(reg, time):
    '''
    checks number of booked seats on the trip using bus_reg number and trip_time
    '''
    trip = []
    bookings = Booking.objects.all()
    for booking in bookings:
        if reg == booking.bus_reg and time == booking.trip_time:
            trip.append({'bus_reg': booking.bus_reg, 'trip_time': booking.trip_time, 'date': booking.trip_date,
                         'ticket_id': booking.ticket_id, 'Customer_name': booking.client_name,
                         'Customer_lastname': booking.client_surname, 'depature': booking.trip_depature,
                         'destination': booking.trip_destination})
    trip = json.dumps({'my_trip': str(trip)})
    trip = json.loads(trip)
    return trip
