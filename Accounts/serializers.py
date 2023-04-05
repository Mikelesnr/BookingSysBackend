from rest_framework import serializers, validators
from .models import User

from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication

from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name","username", "password")
        # extra_kwargs = {
        #     "password": {"write_only": True},
        #     "username": {
        #         "required": True,
        #         "allow_blank": False,
        #         "validators": [
        #             validators.UniqueValidator(
        #                 User.objects.all(), "A user with the Username {} already exists".format(User.username)
        #             )
        #         ],
        #     },
        # }

class AdminRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name","username", "password")
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "A user with the Username {} already exists".format(User.username)
                    )
                ],
            },
        }

    def save(self, **kwargs):
        user = User(
            first_name = self.validated_data.get('first_name'),
            username = self.validated_data.get('username'),
            last_name = self.validated_data.get('last_name'),
            password = make_password(self.validated_data.get('password'))
        )
        
        user.is_admin = True
        user.save()
        if user:
            _, token = AuthToken.objects.create(user)
            print(token)
            print("----------------------------")
            print(str(user) + " registered")

class DriverRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name","username", "password")
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "A user with the Username {} already exists".format(User.username)
                    )
                ],
            },
        }

    def save(self, **kwargs):
        user = User(
            username = self.validated_data.get('username'),
            first_name = self.validated_data.get('first_name'),
            last_name = self.validated_data.get('last_name'),
            password = make_password(self.validated_data.get('password'))
        )
        user.is_driver = True
        user.save()
        if user:
            _, token = AuthToken.objects.create(user)
            print(token)
            print("----------------------------")
            print(str(user) + " registered")

class TravellerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name","username", "password")
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "A user with the Username {} already exists".format(User.username)
                    )
                ],
            },
        }

    def save(self, **kwargs):
        user = User(
            username = self.validated_data.get('username'),
            first_name = self.validated_data.get('first_name'),
            last_name = self.validated_data.get('last_name'),
            password = make_password(self.validated_data.get('password'))
        )
        user.is_traveller = True
        user.save()
        if user:
            _, token = AuthToken.objects.create(user)
            print(token)
            print("----------------------------")
            print(str(user) + " registered")
