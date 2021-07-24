from rest_framework import serializers

from .models import Devices, TempratureReading, HumidityReading

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Devices
        fields = ('uid','name')

