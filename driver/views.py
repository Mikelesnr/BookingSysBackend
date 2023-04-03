from django.http import JsonResponse
from .models import Driver
from .serializers import DriverSerializer


def driver_list(request):
    '''
    .get all the drivers
    .serialize them
    .return json
    '''

    drivers = Driver.objects.all()
    serializer = DriverSerializer(drivers, many=True)
    return JsonResponse(serializer.data, safe=False)
