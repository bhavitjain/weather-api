# Weather API Wrapper Service with Rate Limiting and Caching

This project showcases the development of a Python-based Weather App that interacts with a third-party API to retrieve weather data, incorporates rate limiting to prevent overuse, and leverages Redis for caching to enhance performance and efficiency.

---

## Features

- **Fetch Weather Data**: Retrieves weather data from a third-party API (e.g., [Visual Crossing API](https://www.visualcrossing.com/)).
- **Rate Limiting**: Prevents excessive API usage by limiting the number of requests a client can make within a specified time frame.
- **Caching with Redis**: Stores weather data in Redis with an expiration time to reduce redundant API calls and improve response time.
- **Environment Variables**: Uses `.env` files to securely store sensitive information such as API keys and Redis connection strings.
- **Error Handling**: Graceful error handling for invalid city codes or third-party API downtime.

---

## Requirements

### **System Requirements**
- Python 3.8 or later
- Redis server

### **Python Dependencies**
The project uses the following libraries:
- `FastAPI` - For building the API.
- `Redis` - For caching weather data.
- `requests` - For making HTTP requests to the third-party weather API.

Install the dependencies using pip:
```bash
pip install -r requirements.txt
```

## Installation and Setup
### Clone the Repository:


``` bash
git clone <repository_url>
cd <repository_folder>
```

### install Dependencies:

``` bash
pip install -r requirements.txt
```
Start Redis Server: Ensure that Redis is installed and running locally. You can start Redis using:

``` bash
redis-server
```
Configure Environment Variables: Create a .env file in the project root and add the following variables:

``` env
API-KEY=api-key
EXPIRATION-TIME=43200
REDIS-HOST=localhost
REDIS-PORT=6379
TIME-LIMIT=60
MAX-REQUESTS-PER-WINDOW=10
```

Run the API: Use uvicorn to start the FastAPI server:

``` bash
uvicorn app.main:app --reload
```

## Usage
### Endpoints
Get Weather Data:

```
GET /weather/{city}
```

Fetches weather data for the specified city.

Example: GET /weather/Los_Angeles
Response:

json
```json
{
    "queryCost": 1,
    "latitude": 38.5794,
    "longitude": -121.491,
    "resolvedAddress": "Los_Angeles, United States",
    "address": "Los_Angeles",
    "timezone": "America/Los_Angeles",
    "tzoffset": -8.0,
    "days": [
        {
            "tempmax": 61.1,
            "tempmin": 42.0,
            "temp": 49.8
        }
    ]
}
```

### Rate Limiting:

Clients are allowed a maximum of 10 requests per minute by default.
Exceeding this limit will return a 429 Too Many Requests response.


Sample solution for the [weather-api-wrapper-service](https://roadmap.sh/projects/weather-api-wrapper-service) challenge from [roadmap.sh](https://roadmap.sh/).
