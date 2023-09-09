from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis


async def redis_connect():
    redis = await aioredis.from_url(
        url='redis://localhost:6379',
        encoding='utf-8',
        decode_responses=True,
    )

    FastAPICache.init(RedisBackend(redis), prefix='cache')
