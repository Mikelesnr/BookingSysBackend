from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Accounts.views import (
    registerAdmin, registerDriver, registerTraveller, login)


class TestUrls(SimpleTestCase):

    def test_register_admin_is_resolved(self):
        url = reverse('register_admin')
        print(resolve(url))
        self.assertEquals(resolve(url).func, registerAdmin)

    def test_register_driver_is_resolved(self):
        url = reverse('register_driver')
        print(resolve(url))
        self.assertEquals(resolve(url).func, registerDriver)

    def test_register_user_is_resolved(self):
        url = reverse('register_user')
        print(resolve(url))
        self.assertEquals(resolve(url).func, registerTraveller)

    def test_login_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)
