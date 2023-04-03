from django.urls import path

from . import views

urlpatterns = [
    path("", views.driver_list, name="drivers")
]
