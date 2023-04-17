from django.db import models

# Create your models here


class Driver(models.Model):
    '''
    creates a driver table with buss details and route
    '''
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    bus_reg = models.CharField(max_length=200)
    no_of_seats = models.CharField(max_length=200)
    bus_type = models.CharField(max_length=200)
    route = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} {self.surname} bus reg {self.bus_reg}"
