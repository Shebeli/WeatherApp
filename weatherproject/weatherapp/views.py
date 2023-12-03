from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CityCord
from .serializers import CitySerializer


@api_view(['GET'])
def get_current_weather_info(request):
    if request.method == 'GET':
        requested_city = request.query_params.get('city')
        try:
            city = CityCord.objects.get(name__icontains=requested_city)
        except CityCord.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CitySerializer(city)
        return Response(serializer.data)

