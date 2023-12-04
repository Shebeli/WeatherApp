from typing import Dict
from urllib.parse import urlparse, urlencode

# from weatherproject.settings import OWM_API_KEY, OWM_CURRENT_WEATHER_API
from django.conf import settings


def add_query_params(url: str, params: Dict) -> str: # to be used in later functions
    parsed_url = urlparse(url)
    current_params = dict()
    if parsed_url.query:
        current_params = dict(
            (param.split("=") for param in parsed_url.query.split("&"))
        )
    current_params.update(params)
    updated_query = urlencode(current_params)
    return parsed_url._replace(query=updated_query).geturl()


def current_weather_api_url(
    lat: float, lon: float, part=None, units="metric", lang=None
) -> str:
    return f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={settings.OMW_API_KEY}&units={units}"
