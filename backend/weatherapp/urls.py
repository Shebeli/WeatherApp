from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("current-weather", views.get_current_weather_info),
    path("city-names", views.get_similar_city_names)
]

urlpatterns = format_suffix_patterns(urlpatterns)
