from datetime import datetime
from venv import create
from django.db import models

# Create your models here.


class ApiResponse(models.Model):
    id = models.AutoField(primary_key=True)
    lat = models.CharField(max_length=100, blank=True)
    temperature = models.CharField(max_length=100, blank=True)
    windBearing = models.CharField(max_length=100, blank=True)
    windSpeed = models.CharField(max_length=100, blank=True)
    apparentTemperature = models.CharField(max_length=100, blank=True)
    dewPoint = models.CharField(max_length=100, blank=True)
    pressure = models.CharField(max_length=100, blank=True)
    windGust = models.CharField(max_length=100, blank=True)
    cloudCover = models.CharField(max_length=100, blank=True)
    visibility = models.CharField(max_length=100, blank=True)
    ozone = models.CharField(max_length=100, blank=True)
    humidity = models.CharField(max_length=100, blank=True)
    time = models.CharField(max_length=100, blank=True)
    summary = models.CharField(max_length=100, blank=True)
    icon = models.CharField(max_length=100, blank=True)
    lng = models.CharField(max_length=100, blank=True)
    precipIntensity = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at) + " - " + str(self.id)
