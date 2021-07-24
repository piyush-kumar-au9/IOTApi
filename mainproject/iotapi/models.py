from django.db import models

# Create your models here.
class Devices(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TempratureReading(models.Model):
    device_uid = models.ForeignKey(Devices, on_delete=models.CASCADE)
    temprature = models.CharField(max_length=200)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.device_uid


class HumidityReading(models.Model):
    device_uid = models.ForeignKey(Devices, on_delete=models.CASCADE)
    humidity = models.CharField(max_length=200)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


    def __str__(self):
        return self.device_uid