from .serializers import BookingSerializer
from driver.serializers import BusSerializer
from driver.models import Driver
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .common import open_seats, add_ticket_id, trip_creator

# Create your views here.


@api_view(['GET', 'POST'])
def booking(request, format=None):
    '''
    .get all bookings and creates booking
    .serializes them
    .return json
    '''

    # get bookings
    if request.method == 'GET':
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response({'Bookings': serializer.data}, status=status.HTTP_200_OK)

    # add booking
    if request.method == 'POST':
        bus_reg = request.data.get('bus_reg')
        trip_time = request.data.get('trip_time')
        seats_available = open_seats(bus_reg, trip_time)
        my_request = add_ticket_id(request)
        serializer = BookingSerializer(data=my_request)
        if serializer.is_valid() and seats_available:
            serializer.save()
            return Response({'Booking': my_request, 'Seats available': seats_available}, status=status.HTTP_201_CREATED)
        else:
            return Response({'seats_available': f"{seats_available} seats available"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def buses(request, format=None):
    '''
    .get all buses
    .serializes them
    .return json
    '''

    # get buses
    if request.method == 'GET':
        buses = Driver.objects.all()
        serializer = BusSerializer(buses, many=True)
        return Response({'Buses': serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def trip(request, format=None):
    '''
    .gets all trips
    .serializes them
    .return json
    '''

    # get buses
    if request.method == 'POST':
        bus_reg = request.data.get('bus_reg')
        trip_time = request.data.get('trip_time')
        seats_available = open_seats(bus_reg, trip_time)
        my_trip = trip_creator(bus_reg, trip_time)
        serializer = BusSerializer(buses, many=True)
        return Response({'trip': my_trip, 'Available seats': seats_available}, status=status.HTTP_200_OK)
