from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CityCord
from .serializers import CitySerializer, CityNameSerializer
 
from weatherapp.utils import update_city_weather_data

@api_view(["GET"])
def get_current_weather_info(request, format=None):
    if request.method == "GET":
        requested_city = request.query_params.get("city")
        if not requested_city:
            return Response(data={
                "Error": "No query parameters where provided for city name."
            })
        city = CityCord.objects.filter(name__icontains=requested_city).first()
        if not city: 
            return Response(status=status.HTTP_404_NOT_FOUND)
        update_city_weather_data(city)
        serialized_instance = CitySerializer(city)
        return Response(serialized_instance.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_similar_city_names(request, format=None):
    if request.method == "GET":
        requested_city = request.query_params.get("city")
        if not requested_city:
            return Response(data={
                "Error": "No query parameters where provided for city name."
            })
        cities = CityCord.objects.filter(name__icontains=requested_city)[:10]      
        serialized_city_names = CityNameSerializer(cities, many=True)
        return Response(serialized_city_names.data, status=status.HTTP_200_OK)