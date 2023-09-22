from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from app.settings.config import settings


async def redis_setup():
    redis = await aioredis.from_url(
        url=f'{settings().REDIS_HOST}:{settings().REDIS_PORT}',
        encoding='utf-8',
        decode_responses=True,
    )

    FastAPICache.init(RedisBackend(redis), prefix='cache')
