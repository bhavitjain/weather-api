import redis

from config import REDIS_PORT, REDIS_HOST


def create_redis():
  return redis.ConnectionPool(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=0,
    decode_responses=True
  )

pool = create_redis()

def get_redis():
  # Here, we re-use our connection pool
  # not creating a new one
  return redis.Redis(connection_pool=pool)
