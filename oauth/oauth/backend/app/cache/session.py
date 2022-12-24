import redis

from app.core.config import settings

client = redis.Redis(host=settings.CACHE_HOST, port=settings.CACHE_PORT, db=0)
