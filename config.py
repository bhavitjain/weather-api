import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API-KEY")
EXPIRATION_TIME = int(os.getenv("EXPIRATION-TIME"))
TIME_LIMIT = int(os.getenv("TIME-LIMIT", "60"))
MAX_REQUESTS_PER_WINDOW = int(os.getenv("MAX-REQUESTS-PER-WINDOW", "1"))