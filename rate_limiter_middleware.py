import time
from http import HTTPStatus

from requests import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from config import TIME_LIMIT, MAX_REQUESTS_PER_WINDOW

request_counter: int = 0
last_request_time: float = time.time()


class RateLimiterMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        global last_request_time, request_counter

        current_time = time.time()
        if current_time - last_request_time > TIME_LIMIT:
            request_counter = 0
            last_request_time = current_time

        request_counter += 1

        if request_counter > MAX_REQUESTS_PER_WINDOW:
            return JSONResponse({"message": "Rate limit exceeded", "status_code": HTTPStatus.TOO_MANY_REQUESTS},
                                status_code=HTTPStatus.TOO_MANY_REQUESTS)

        response = await call_next(request)
        return response
