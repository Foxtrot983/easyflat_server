import redis
from django.conf import settings

def redis_connect():
    redis_instance = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
    return redis_instance