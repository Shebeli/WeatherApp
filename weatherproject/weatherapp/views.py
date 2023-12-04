import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CityCord, CityWeather, CityWeatherCondition, CityWind
from .serializers import CitySerializer
from weatherproject.utils.owm_api import current_weather_api_url

@api_view(['GET'])
def get_current_weather_info(request, format=None):
    if request.method == 'GET':
        requested_city = request.query_params.get('city')
        if not requested_city:
            return Response(data={'error': 'no query params provided for "city"'})
        try:
            city = CityCord.objects.get(name__icontains=requested_city)
        except CityCord.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if city.is_data_old:
            
        serializer = CitySerializer(city)
        return Response(serializer.data)

# def update_weather_data(city: CityCord):
#     response = requests.get(current_weather_api_url)
#     weather_data = dict(response.json())
#     for 