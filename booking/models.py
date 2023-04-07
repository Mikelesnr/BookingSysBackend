from django.db import models

# Create your models here.

# creates table of bookings


class Booking(models.Model):
    client_name = models.CharField(max_length=200)
    client_surname = models.CharField(max_length=200)
    bus_reg = models.CharField(max_length=200)
    trip_time = models.CharField(max_length=200)
    trip_date = models.CharField(max_length=200)
    ticket_id = models.CharField(max_length=200)
    trip_depature = models.CharField(max_length=500)
    trip_destination = models.CharField(max_length=500)
