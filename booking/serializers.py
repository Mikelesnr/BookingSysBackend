from rest_framework import serializers
from .models import Booking
from .models import Trip


class BookingSerializer(serializers.ModelSerializer):
    '''
    serializes Tickets to and from json
    '''
    class Meta:
        model = Booking
        fields = ['client_name', 'client_surname', 'bus_reg', 'trip_time', 'trip_date',
                  'ticket_id', 'trip_depature', 'trip_destination']


class TripSerializer(serializers.ModelSerializer):
    '''
    serializes Tickets to and from json
    '''
    class Meta:
        model = Trip
        fields = ['bus_reg', 'trip_time', 'trip_date',
                  'trip_depature', 'trip_destination']
