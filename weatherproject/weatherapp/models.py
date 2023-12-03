from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    MinValueValidator,
    MaxValueValidator,
)


class CityCord(models.Model):
    name = models.CharField(max_length=20, unique=True)
    country = models.CharField(max_length=2)
    lat = models.DecimalField("latitude", max_digits=16, decimal_places=15)
    lon = models.DecimalField("longitude", max_digits=16, decimal_places=15)

class CityImportStatus(models.Model):
    is_imported = models.BooleanField(default=False)

class CityWeather(models.Model):
    city = models.OneToOneField(CityCord, on_delete=models.CASCADE)
    temp = models.DecimalField(max_digits=3, decimal_places=2)
    feels_like = models.DecimalField(max_digits=3, decimal_places=2)
    temp_min = models.DecimalField(max_digits=3, decimal_places=2)
    temp_max = models.DecimalField(max_digits=3, decimal_places=2)
    pressure = models.IntegerField()
    humidity = models.IntegerField()
    uv_index = models.DecimalField(max_digits=3, decimal_places=2)


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
    wind_speed = models.DecimalField(max_digits=3, decimal_places=2)
    wind_deg = models.DecimalField(max_digits=3,decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(360)]
    )
    clouds = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    visibility = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10000)]
    )
