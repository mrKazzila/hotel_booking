from typing import Type, TypeVar

from sqlalchemy import select, insert

from app.settings.database import Base, async_session_maker

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

    @classmethod
    async def add_entity(cls, **data):
        async with async_session_maker() as session:
            query = (
                insert(cls.model).values(**data)
            )

            await session.execute(query)
            await session.commit()
