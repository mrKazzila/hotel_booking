from app.settings.database import async_session_maker
from sqlalchemy import select
from app.settings.database import Base

from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union


ModelType = TypeVar("ModelType", bound=Base)


class BaseServices:
    model: Type[ModelType] = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .filter_by(id=model_id)
            )
            result = await session.execute(query)

            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .filter_by(**filter_by)
            )
            result = await session.execute(query)

            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
            )
            result = await session.execute(query)

            return result.mappings().all()

