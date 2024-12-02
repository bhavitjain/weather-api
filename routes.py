from fastapi import APIRouter

from weather_service import call_weather_service_api

weather_api_router = APIRouter()


@weather_api_router.get("/{city}")
def get_weather_data(city: str):
    response = call_weather_service_api(city)
    return response
