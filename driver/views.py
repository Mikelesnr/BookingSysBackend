from .models import Driver
from .serializers import DriverSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Api.base_models import BaseModel
from booking.serializers import TripSerializer
from booking.models import Trip


@api_view(['GET', 'POST'])
def driver_list(request, format=None):
    '''
    .get all the drivers and adds driver
    .serialize them
    .return json
    '''

    driver_model = BaseModel(
        model=Driver, serializer=DriverSerializer, request=request)

    # get drivers
    if request.method == 'GET':
        return Response(driver_model.get_all(), status=status.HTTP_200_OK)

    # add drivers
    if request.method == 'POST':
        if driver_model:
            return Response(driver_model.add(), status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def driver_detail(request, id, format=None):
    '''
    .gets one driver, update driver, delete driver
    .serializes record
    .return json
    '''

    driver_model = BaseModel(
        model=Driver, serializer=DriverSerializer, request=request)

    # retrieve driver and assign to driver
    try:
        driver = Driver.objects.get(pk=id)
    except Driver.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get driver
    if request.method == 'GET':
        return Response(driver_model.get_one(driver), status=status.HTTP_200_OK)

    # edit driver
    elif request.method == 'PUT':
        return Response(driver_model.edit_entry(driver), status=status.HTTP_201_CREATED)

    # delete driver
    elif request.method == 'DELETE':
        Trip.objects.filter(bus_reg=driver.bus_reg).delete()
        driver_model.delete_entry(driver)
        return Response(status=status.HTTP_204_NO_CONTENT)
