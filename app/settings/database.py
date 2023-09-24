from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.settings.config import settings

if settings().MODE == 'TEST':
    DATABASE_URL = str(settings().test_database_url)
    DATABASE_PARAMS = {'poolclass': NullPool}
else:
    DATABASE_URL = str(settings().database_url)
    DATABASE_PARAMS = {}

engine: AsyncEngine = create_async_engine(url=DATABASE_URL, **DATABASE_PARAMS)
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
