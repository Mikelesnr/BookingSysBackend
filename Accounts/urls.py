from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('register/admin/', views.registerAdmin, name='register_admin'),
    path('register/driver/', views.registerDriver, name='register_driver'),
    path('register/traveller/', views.registerTraveller, name='register_user'),
    path('auth/login/', views.login, name='login'),
    path('profile/', views.get_user),
    path('users/', views.user_list),
    path("users/<int:id>", views.user_detail,),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall')
]
