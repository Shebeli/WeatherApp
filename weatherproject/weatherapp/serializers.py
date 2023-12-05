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
    city_weather = CityWeatherSerializer()
    city_weather_condition = CityWeatherConditionSerializer()
    city_wind = CityWindSerializer()

    class Meta:
        model = CityCord
        exclude = ['lat', 'lon']

    # def get_city_weather(self, obj):
    #     city_weather_obj = CityWeather.objects.filter(city=obj).first()
    #     if city_weather_obj:
    #         return CityWeatherSerializer(city_weather_obj.first()).data
    #     return CityWeatherSerializer().data
    
    # def get_city_weather_condition(self, obj):
    #     city_weather_condition_obj = CityWeatherCondition.objects.filter(city=obj).first()
    #     if city_weather_condition_obj:
    #         return CityWeatherConditionSerializer(city_weather_condition_obj.first()).data
    #     return CityWeatherSerializer().data
    
    # def get_city_wind(self, obj):
    #     city_wind_condition_obj = CityWind.objects.filter(city=obj).first()
    #     if city_wind_condition_obj:
    #         return CityWindSerializer(city_wind_condition_obj).data
    #     return CityWindSerializer().data