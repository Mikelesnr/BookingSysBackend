from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    is_traveller = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username
    

class AdminUser(models.Model):
    user = models.OneToOneField(User,related_name="AdminUser",on_delete=models.CASCADE)
    username = models.CharField(max_length=25, blank=True, null=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=12, blank=True, null=True)
    


class Driver(models.Model):
    user = models.OneToOneField(User,related_name="Driver",on_delete=models.CASCADE)
    username = models.CharField(max_length=25, blank=True, null=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=12, blank=True, null=True)


class Traveller(models.Model):
    user = models.OneToOneField(User,related_name="Traveller",on_delete=models.CASCADE)
    username = models.CharField(max_length=25, blank=True, null=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=12, blank=True, null=True)