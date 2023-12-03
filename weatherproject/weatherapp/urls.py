from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", views.get_current_weather_info)
]

urlpatterns = format_suffix_patterns(urlpatterns)