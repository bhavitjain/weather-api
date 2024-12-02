from fastapi import FastAPI
from fastapi.responses import JSONResponse
from requests import Request

from rate_limiter_middleware import RateLimiterMiddleware
from routes import weather_api_router
from weather_api_exception import WeatherApiException

app = FastAPI()

app.add_middleware(RateLimiterMiddleware)

@app.exception_handler(WeatherApiException)
async def weather_api_exception_handler(request: Request, exc: WeatherApiException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message, "status_code": exc.status_code},
    )


app.include_router(prefix="/weather", tags=["Weather API"], router=weather_api_router)
