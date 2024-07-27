from django.contrib import admin
from .models import SosMessage, SosUser

# Register your models here.
admin.site.register(SosMessage)
admin.site.register(SosUser)