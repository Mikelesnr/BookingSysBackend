from rest_framework import serializers
from .models import Driver


class DriverSerializer(serializers.ModelSerializer):
    '''
    serializes drivers to JSON
    '''
    class Meta:
        model = Driver
        fields = ['id', 'name', 'surname', 'bus_reg',
                  'no_of_seats', 'bus_type', 'route']
