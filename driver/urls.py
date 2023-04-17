from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.driver_list, name="drivers"),
    path("<int:id>", views.driver_detail, name="driver")
]

urlpatterns = format_suffix_patterns(urlpatterns)
