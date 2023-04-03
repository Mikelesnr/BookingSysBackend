from django.http import JsonResponse
from .models import Driver
from .serializers import DriverSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def driver_list(request):
    '''
    .get all the drivers
    .serialize them
    .return json
    '''

    # get drivers
    if request.method == 'GET':
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return JsonResponse({'drivers': serializer.data})

    # add drivers
    if request.method == 'POST':
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
