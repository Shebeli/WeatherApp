from django.urls import path 

from . import views

urlpatterns = [
    path("", views.get_current_weather_info, name="get_current_weather_info")
]