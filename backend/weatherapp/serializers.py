from rest_framework import serializers
from .models import (CityCord, 
                     CityWeatherCondition, 
                     CityWeather, 
                     CityWind)


class CityWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityWeather
        exclude = ['city', 'id']

class CityWeatherConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityWeatherCondition
        exclude = ['city', 'id']

class CityWindSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityWind
        exclude = ['city', 'id']

class CitySerializer(serializers.ModelSerializer):
    cityweather = CityWeatherSerializer()
    cityweathercondition = CityWeatherConditionSerializer()
    citywind = CityWindSerializer()

    class Meta:
        model = CityCord
        exclude = ['lat', 'lon']

class CityNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CityCord
        fields = ['id', 'name']

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