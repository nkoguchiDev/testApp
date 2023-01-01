import redis

from app.core.config import settings

connection = redis.Redis(
    host=settings.CACHE_HOST,
    port=settings.CACHE_PORT,
    db=0)
