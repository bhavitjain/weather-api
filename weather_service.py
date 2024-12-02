import json
import logging
from http import HTTPStatus
from json import JSONDecodeError

import requests
from requests.exceptions import InvalidURL, HTTPError

from config import API_KEY, EXPIRATION_TIME
from constants import WEATHER_API_BASE_URL
from weather_api_exception import WeatherApiException

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def call_weather_service_api(city: str, cache):
    try:
        if cache.get(city):
            json_string = cache.get(city)
            return json.loads(json_string)
        response = requests.get(WEATHER_API_BASE_URL.format(city=city, api_key=API_KEY))
        response.raise_for_status()
        cache.set(city, response.text, ex=EXPIRATION_TIME)
        return response.json()

    except HTTPError as e:
        logger.error(f"HTTP Error Occurred: {str(e)}")
        raise WeatherApiException(
            message=f"HTTP Error Occurred: {str(e)}",
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR
        )
    except InvalidURL as e:
        logger.error(f"Invalid URL: {str(e)}")
        raise WeatherApiException(
            message=f"Invalid URL: {str(e)}",
            status_code=HTTPStatus.BAD_REQUEST
        )
    except JSONDecodeError as e:
        logger.error(f"JSON Decode Error: {str(e)}")
        raise WeatherApiException(
            message=f"JSON Decode Error: {str(e)}",
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR
        )
    except Exception as e:
        logger.exception(f"Unexpected Error Occurred: {str(e)}")
        raise WeatherApiException(
            message=f"Unexpected Error Occurred: {str(e)}",
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR
        )
