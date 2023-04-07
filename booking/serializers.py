from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    '''
    serializes Tickets to JSON
    '''
    class Meta:
        model = Booking
        fields = ['client_name', 'client_surname', 'bus_reg',
                  'trip_time', 'trip_date', 'ticket_id', 'trip_depature', 'trip_destination']
