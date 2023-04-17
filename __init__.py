from driver.models import Driver
from driver.serializers import DriverSerializer

drivers = Driver.objects.all()
driver_serializer = DriverSerializer(drivers, many=True)
