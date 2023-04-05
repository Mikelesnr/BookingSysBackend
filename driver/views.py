from .models import Driver
from .serializers import DriverSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def driver_list(request, format=None):
    '''
    .get all the drivers and adds driver
    .serialize them
    .return json
    '''

    # get drivers
    if request.method == 'GET':
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # add drivers
    if request.method == 'POST':
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def driver_detail(request, id, format=None):
    '''
    .gets one driver, update driver, delete driver
    .serializes record
    .return json
    '''

    # retrieve driver and assign to driver
    try:
        driver = Driver.objects.get(pk=id)
    except Driver.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get driver
    if request.method == 'GET':
        serializer = DriverSerializer(driver)
        return Response(serializer.data)

    # edit driver
    elif request.method == 'PUT':
        serializer = DriverSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete driver
    elif request.method == 'DELETE':
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
