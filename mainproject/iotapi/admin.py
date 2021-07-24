from django.contrib import admin

from .models import Devices, TempratureReading, HumidityReading
# Register your models here.
admin.site.register([Devices, TempratureReading, HumidityReading])