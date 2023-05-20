from django.shortcuts import render

# Create your views here.
from .models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication

# from rest_framework.authtoken.models import Token
from .serializers import AdminRegisterSerializer, TravellerRegisterSerializer,\
    DriverRegisterSerializer, UserSerializer


@api_view(['GET'])
def user_list(request, format=None):
    if request.method == 'GET':
        users = User.objects.filter(is_staff=False)
        serializer = UserSerializer(users, many=True)
        return Response((serializer.data))
    
@api_view(['GET','DELETE'])
def user_detail(request, id, format=None):
    user = User.objects.get(pk=id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response((serializer.data))
    
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name
        },
        'token': token,
        "Message": "Logged in successfully",
        # "is_admin" : user.is_admin
    })

# Retrieve user profile
@api_view(['GET'])
def get_user(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'user': {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'user-type': "Admin" if user.is_admin\
                else "Driver" if user.is_driver else "Traveller" if user.is_traveller\
                    else "User-role not specified"
        }
        })
    return Response({'error':'Not authorized'}, status=400)
