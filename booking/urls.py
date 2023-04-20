from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.booking, name="booking"),
    path("buses", views.buses, name="buses"),
    path("trip", views.trip, name="trip"),
    path("seats", views.seats_available, name="seats"),
    path("tripsavailable", views.trips, name="trips"),
    path("booking/<int:id>", views.booking_edit, name="booking_manage"),
    path("trips/<int:id>", views.trip_edit, name="trip_manage"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
