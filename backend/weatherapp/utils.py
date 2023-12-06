import requests
from typing import Dict, Tuple
from datetime import datetime

from .models import CityCord, CityWeather, CityWeatherCondition, CityWind
from weatherproject.utils.owm_api import current_weather_api_url


def update_city_weather_data(
    city: CityCord,
) -> Tuple[CityWeather, CityWeatherCondition, CityWind]:
    if city.is_data_old():
        response = requests.get(current_weather_api_url(city.lat, city.lon))
        if response.status_code != 200:
            raise Exception(f"Request to OWM API has failed. text:\n {response.text}")
        response_data = response.json()
        city_weather = _get_or_create_cityweather(city, response_data)
        city_weather_condition = _get_or_create_cityweathercondition(
            city, response_data
        )
        city_wind = _get_or_create_citywind(city, response_data)
        city.last_updated = datetime.now()
        city.save()
        return (city_weather, city_weather_condition, city_wind)


def get_weather_data(
    city: CityCord,
) -> Tuple[CityWeather, CityWeatherCondition, CityWind]:
    updated_data = update_city_weather_data(city)
    if not updated_data:
        return (
            city.cityweather_set.first(),
            city.cityweathercondition_set.first(),
            city.citywind_set.first(),
        )
    return updated_data


def _get_or_create_cityweather(city: CityCord, response_data: Dict) -> CityWeather:
    weather_data = response_data["main"]
    city_weather_obj = CityWeather.objects.filter(city=city).first()
    if not city_weather_obj:
        city_weather_obj = CityWeather.objects.create(
            city=city,
            temp=weather_data["temp"],
            feels_like=weather_data["feels_like"],
            temp_min=weather_data["temp_min"],
            temp_max=weather_data["temp_max"],
            pressure=weather_data["pressure"],
            humidity=weather_data["humidity"],
        )
    return city_weather_obj


def _get_or_create_cityweathercondition(
    city: CityCord, response_data: Dict
) -> CityWeatherCondition:
    weather_condition_data = response_data["weather"][0]
    city_weather_condition_obj = CityWeatherCondition.objects.filter(city=city).first()
    if not city_weather_condition_obj:
        city_weather_condition_obj = CityWeatherCondition.objects.create(
            city=city,
            weather_id=weather_condition_data["id"],
            main=weather_condition_data["main"],
            description=weather_condition_data["description"],
            icon=weather_condition_data["icon"],
        )
    return city_weather_condition_obj


def _get_or_create_citywind(city: CityCord, response_data: Dict) -> CityWind:
    city_wind_obj = CityWind.objects.filter(city=city).first()
    if not city_wind_obj:
        city_wind_obj = CityWind.objects.create(
            city=city,
            wind_speed=response_data["wind"]["speed"],
            wind_deg=response_data["wind"]["deg"],
            clouds=response_data["clouds"]["all"],
            visibility=response_data["visibility"],
        )
    return city_wind_obj
