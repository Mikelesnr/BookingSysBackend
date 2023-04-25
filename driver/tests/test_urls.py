from django.test import SimpleTestCase
from django.urls import reverse, resolve
from driver.views import (driver_list, driver_detail)


class TestUrls(SimpleTestCase):

    def test_drivers_is_resolved(self):
        url = reverse('drivers')
        print(resolve(url))
        self.assertEquals(resolve(url).func, driver_list)

    # def test_driver_is_resolved(self):
    #     url = reverse('driver')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func, driver_detail)
