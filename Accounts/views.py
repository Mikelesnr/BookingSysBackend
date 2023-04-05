from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication

# from rest_framework.authtoken.models import Token
from .serializers import AdminRegisterSerializer, TravellerRegisterSerializer,\
    DriverRegisterSerializer, UserSerializer


@api_view(['POST'])
def registerAdmin(request):
    serializer = AdminRegisterSerializer(data=request.data)
    # print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer_data = serializer.data
        print(serializer_data)
        user = serializer.save()
        # _, token = AuthToken.objects.create(user)
        return Response({
            "user_info": serializer_data,
            # "token": token
            "Message": "Successfully registered"
        })

@api_view(['POST'])
def registerDriver(request):
    serializer = DriverRegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer_data = serializer.data
        print(serializer_data)
        user = serializer.save()
        return Response({
            "user_info": serializer_data,
            # "token": token
            "Message": "Successfully registered"
        })
@api_view(['POST']) 
def registerTraveller(request):
    serializer = TravellerRegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer_data = serializer.data
        user = serializer.save()
        return Response({
            "user_info": serializer_data,
            # "token": token
            "Message": "Successfully registered"
        })
    


# User login view

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    # print(serializer)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    # print(user)
    _, token = AuthToken.objects.create(user)
    return Response({
        'user': {
            'username': user.username
        },
        'token': token,
        "Message": "Logged in successfully",
        # "is_admin" : user.is_admin
    })
