from django.contrib import admin
from .models import User, AdminUser, Traveller, Driver

# Register your models here.

admin.site.register(User)
admin.site.register(Driver)
admin.site.register(AdminUser)
admin.site.register(Traveller)
