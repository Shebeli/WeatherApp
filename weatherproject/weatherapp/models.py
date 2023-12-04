import requests
from datetime import datetime, timedelta

from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    MinValueValidator,
    MaxValueValidator,
)
# from weatherproject.utils.owm_api import current_weather_api_url

class CityCord(models.Model):
    name = models.CharField(max_length=70, unique=True)
    country = models.CharField(max_length=5)
    lat = models.FloatField("latitude")
    lon = models.FloatField("longitude")
    last_updated = models.DateTimeField(null=True, blank=True)

# def get_weather_data(self):
#     response = requests.get(current_weather_api_url(self.lat, self.lon))
#     return

def is_data_old(self, time_threshold=timedelta(minutes=30)):
    if not self.last_updated:
        return True
    if datetime.now() - time_threshold > self.last_updated:
        return True

class CityImportStatus(models.Model):
    is_imported = models.BooleanField(default=False)


class CityWeather(models.Model):
    city = models.OneToOneField(CityCord, on_delete=models.CASCADE)
    temp = models.FloatField()
    feels_like = models.FloatField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()
    uv_index = models.FloatField(blank=True, null=True)


class CityWeatherCondition(models.Model):
    city = models.OneToOneField(CityCord, on_delete=models.CASCADE)
    weather_id = models.IntegerField(
        validators=[MinValueValidator(200), MaxValueValidator(804)]
    )  # a code defined by openweatherAPI representing the weather condition which the length is always 3.
    main = models.CharField("main condition", max_length=20)
    description = models.CharField(max_length=50)
    icon = models.CharField(
        validators=[MinLengthValidator(3), MaxLengthValidator(3)]
    )  # has the following format: 01d, 04d, 50d, etc.


class CityWind(models.Model):
    city = models.OneToOneField(CityCord, on_delete=models.CASCADE)
    wind_speed = models.FloatField()
    wind_deg = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(360)]
    )
    clouds = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    visibility = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10000)]
    )
