from .serializers import BookingSerializer
from driver.serializers import BusSerializer
from driver.models import Driver
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
import json
from .common import open_seats

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
        serializer = BookingSerializer(data=request.data)
        # and open_seats(request.data.reg, request.data.time):
        if serializer.is_valid() and seats_available:
            serializer.save()
            return Response({'Booking': serializer.data, 'Seats available': seats_available}, status=status.HTTP_201_CREATED)
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


@api_view(['GET', 'POST'])
def common(request, format=None):
    '''
    .get all buses
    .serializes them
    .return json
    '''

    # get buses
    if request.method == 'GET':
        buses = Driver.objects.all()
        serializer = BusSerializer(buses, many=True)
        return Response({'Buses': serializer.data, 'Open seats': open_seats("ABB 12346", "1pm")}, status=status.HTTP_200_OK)
