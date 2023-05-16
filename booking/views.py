from .serializers import BookingSerializer, TripSerializer
from driver.serializers import BusSerializer
from driver.models import Driver
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Booking, Trip
from .common import open_seats, add_ticket_id, trip_creator, seats
from Api.base_models import BaseModel
import json
from django.db.models import Count


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
        return Response(booking_model.get_all(), status=status.HTTP_200_OK)

    # add booking
    if request.method == 'POST':
        bus_reg = request.data.get('bus_reg')
        trip_time = request.data.get('trip_time')
        seats_available = open_seats(bus_reg, trip_time)
        my_request = add_ticket_id(request)
        serializer = BookingSerializer(data=my_request)
        if serializer.is_valid() and seats_available:
            serializer.save()
            my_request['seats'] = seats_available-1
            return Response(my_request, status=status.HTTP_201_CREATED)
        else:
            return Response({'seats_available': f"{seats_available} seats available"}, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def booking_edit(request, id, format=None):
    '''
    .gets one driver, update driver, delete driver
    .serializes record
    .return json
    '''

    booking_model = BaseModel(
        model=Booking, serializer=BookingSerializer, request=request)

    # retrieve driver and assign to driver
    try:
        booking = Booking.objects.get(pk=id)
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get driver
    if request.method == 'GET':
        return Response(booking_model.get_one(booking), status=status.HTTP_200_OK)

    # edit driver
    elif request.method == 'PUT':
        return Response(booking_model.edit_entry(booking), status=status.HTTP_201_CREATED)

    # delete driver
    elif request.method == 'DELETE':
        booking_model.delete_entry(booking)
        return Response(status=status.HTTP_204_NO_CONTENT)


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
        return Response(bus_model.get_all(), status=status.HTTP_200_OK)


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
        # seats_available = open_seats(bus_reg, trip_time)
        trip = trip_creator(bus_reg, trip_time)
        return Response(trip, status=status.HTTP_200_OK)


@api_view(['POST'])
def seats_available(request, format=None):
    '''
    returns the seats avaible on a trip
    '''
    if request.method == 'POST':
        bus_reg = request.data.get('bus_reg')
        trip_time = request.data.get('trip_time')
        seats_available = open_seats(bus_reg, trip_time)
        return Response({'seats': seats_available}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def trips(request, format=None):
    '''
    .get all trips and creates tips
    .serializes them
    .return json
    '''

    trip_model = BaseModel(
        model=Trip, serializer=TripSerializer, request=request)

    # get trips
    if request.method == 'GET':
        my_models = []
        serializer = TripSerializer(Trip.objects.all(), many=True)
        models = serializer.data
        for model in models:
            new_model = seats(model)
            my_models.append(new_model)
        my_models = my_models
        return Response(my_models, status=status.HTTP_200_OK)

    # add trip
    if request.method == 'POST':
        if trip_model:
            return Response(trip_model.add(), status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def trip_edit(request, id, format=None):
    '''
    .gets one driver, update driver, delete driver
    .serializes record
    .return json
    '''

    trip_model = BaseModel(
        model=Trip, serializer=TripSerializer, request=request)

    # retrieve driver and assign to driver
    try:
        trip = Trip.objects.get(pk=id)
    except Driver.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get driver
    if request.method == 'GET':
        return Response(trip_model.get_one(trip), status=status.HTTP_200_OK)

    # edit driver
    elif request.method == 'PUT':
        return Response(trip_model.edit_entry(trip), status=status.HTTP_201_CREATED)

    # delete driver
    elif request.method == 'DELETE':
        Booking.objects.filter(bus_reg=trip.bus_reg,
                               trip_time=trip.trip_time).delete()
        trip_model.delete_entry(trip)
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def bus_trip_count(request):
    trips = Trip.objects.values('bus_reg').annotate(total_trips=Count('id'))
    res_data = list(trips)
    return Response(res_data)


@api_view(['GET'])
def bus_booking_count(request):
    bookings = Booking.objects.values('bus_reg').annotate(total_bookings=Count('id'))
    response_data = list(bookings)
    return Response(response_data)
