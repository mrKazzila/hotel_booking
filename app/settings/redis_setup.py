from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis
from app.settings.config import settings


async def redis_setup():
    redis = await aioredis.from_url(
        url='redis://localhost:6379',  # TODO: move to env
        encoding='utf-8',
        decode_responses=True,
    )

    FastAPICache.init(RedisBackend(redis), prefix='cache')
