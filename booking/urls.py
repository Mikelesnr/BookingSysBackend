from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.booking, name="booking"),
    path("buses", views.buses, name="buses"),
    path("trip", views.trip, name="trip"),
    path("seats", views.seats_available, name="seats")
]

urlpatterns = format_suffix_patterns(urlpatterns)
