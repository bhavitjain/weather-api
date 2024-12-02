from fastapi import APIRouter, Depends

from db import get_redis
from weather_service import call_weather_service_api

weather_api_router = APIRouter()


@weather_api_router.get("/{city}")
def get_weather_data(city: str, cache = Depends(get_redis)):
    response = call_weather_service_api(city, cache)
    return response
