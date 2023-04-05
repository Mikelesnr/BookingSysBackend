from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('register/admin/', views.registerAdmin),
    path('register/driver/', views.registerDriver),
    path('register/traveller/', views.registerTraveller),
    path('auth/login/', views.login),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall')
]
