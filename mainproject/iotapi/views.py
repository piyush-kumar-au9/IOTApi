from django.shortcuts import render

from rest_framework import viewsets
from .models import Devices, TempratureReading, HumidityReading
from .serializers import DeviceSerializer
# Create your views here.

class DeviceViewSet(viewsets.ModelViewSet):

    serializer_class = DeviceSerializer
    lookup_field = "uid"
    def get_queryset(self):
        queryset = Devices.objects.all()
        if self.kwargs.get('uid'):
            uid = int(self.kwargs.get('uid'))
            queryset = Devices.objects.filter(uid = uid)
        return queryset

    