from .serializers import BookingSerializer, TripSerializer
from driver.serializers import BusSerializer
from driver.models import Driver
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Booking, Trip
from .common import open_seats, add_ticket_id, trip_creator
from Api.base_models import BaseModel

# Create your views here.


@api_view(['GET', 'POST'])
def booking(request, format=None):
    '''
    .get all bookings and creates booking
    .serializes them
    .return json
    '''

    booking_model = BaseModel(
        model=Booking, serializer=BookingSerializer, request=request)

    # get bookings
    if request.method == 'GET':
        return Response({'Bookings': booking_model.get_all()}, status=status.HTTP_200_OK)

    # add booking
    if request.method == 'POST':
        bus_reg = request.data.get('bus_reg')
        trip_time = request.data.get('trip_time')
        seats_available = open_seats(bus_reg, trip_time)
        my_request = add_ticket_id(request)
        booking_model_post = BaseModel(
            model=Booking, serializer=BookingSerializer, request=my_request)
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

    bus_model = BaseModel(
        model=Driver, serializer=BusSerializer, request=request)

    # get buses
    if request.method == 'GET':
        return Response({'Buses': bus_model.get_all()}, status=status.HTTP_200_OK)


@api_view(['POST'])
def trip(request, format=None):
    '''
    .gets all trips
    .serializes them
    .return json
    '''

    # get trip
    if request.method == 'POST':
        bus_reg = request.data.get('bus_reg')
        trip_time = request.data.get('trip_time')
        seats_available = open_seats(bus_reg, trip_time)
        my_trip = trip_creator(bus_reg, trip_time)
        return Response({'trip': my_trip, 'Available seats': seats_available}, status=status.HTTP_200_OK)


@api_view(['POST'])
def seats_available(request, format=None):
    '''
    returns the seats avaible on a trip
    '''
    if request.method == 'POST':
        bus_reg = request.data.get('bus_reg')
        trip_time = request.data.get('trip_time')
        seats_available = open_seats(bus_reg, trip_time)
        return Response({'Available seats': seats_available}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def trips(request, format=None):
    '''
    .get all trips and creates tips
    .serializes them
    .return json
    '''

    trip_model = BaseModel(
        model=Trip, serializer=TripSerializer, request=request)

    # get trip
    if request.method == 'GET':
        return Response({'Bookings': trip_model.get_all()}, status=status.HTTP_200_OK)

    # add trip
    if request.method == 'POST':
        if trip_model:
            return Response(trip_model.add(), status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def trip_edit(request, id, format=None):
    '''
    .gets one trip, updates trip details, deletes trip
    .serializes record
    .return json
    '''

    trip_model = BaseModel(
        model=Trip, serializer=TripSerializer, request=request)

    # retrieve driver and assign to driver
    try:
        reg = request.data.get('bus_reg')
        time = request.data.get('trip_time')
        trip = Trip.objects.get(bus_reg=reg, trip_time=time)
    except Trip.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get driver
    if request.method == 'GET':
        return Response(trip_model.get_one(trip), status=status.HTTP_200_OK)

    # edit driver
    elif request.method == 'PUT':
        return Response(trip_model.edit_entry(trip), status=status.HTTP_201_CREATED)

    # delete driver
    elif request.method == 'DELETE':
        trip_model.delete_entry(trip)
        return Response(status=status.HTTP_204_NO_CONTENT)
