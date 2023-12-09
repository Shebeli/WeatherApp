from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

weatherapp_route = routers.DefaultRouter()
weatherapp_route.register(r"get-current", views.get_current_weather_info)
weatherapp_route.register(r"get-similar-city-names", views.get_similar_city_names)


# urlpatterns = [
#     path("current", views.get_current_weather_info),
#     path("city-names", views.get_similar_city_names)
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
