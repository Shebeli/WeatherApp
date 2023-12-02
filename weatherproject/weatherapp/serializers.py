from rest_framework import serializers
from .models import (CityCord, 
                     CityWeatherCondition, 
                     CityWeather, 
                     CityWind)


class CityWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityWeather
        exclude = ['city']

class CityWeatherConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityWeatherCondition
        exclude = ['city']

class CityWindSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityWind
        exclude = ['city']

class CitySerializer(serializers.ModelSerializer):
    city_weather = serializers.SerializerMethodField()
    city_weather_condition = serializers.SerializerMethodField()
    city_wind = serializers.SerializerMethodField()

    class Meta:
        model = CityCord
        exclude = ['lat', 'lon']

    def get_city_weather(self, obj):
        city_weather_obj = CityWeather.objects.get(citycord=obj)
        return CityWeatherSerializer(city_weather_obj).data
    
    def get_city_weather_condition(self, obj):
        city_weather_condition_obj = CityWeatherCondition.objects.get(citycord=obj)
        return CityWeatherConditionSerializer(city_weather_condition_obj).data
    
    def get_city_wind(self, obj):
        city_wind_condition_obj = CityWind.objects.get(citycord=obj)
        return CityWindSerializer(city_wind_condition_obj).data
    