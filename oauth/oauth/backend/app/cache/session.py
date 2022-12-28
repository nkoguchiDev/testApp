import redis

from app.core.config import settings

cache = redis.Redis(host=settings.CACHE_HOST, port=settings.CACHE_PORT, db=0)
