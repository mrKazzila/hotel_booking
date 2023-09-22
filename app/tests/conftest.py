import asyncio
import json
from asyncio import BaseEventLoop
from datetime import datetime

import pytest
from httpx import AsyncClient
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import base
from app.main import app as fastapi_app
from app.settings.config import settings
from app.settings.database import Base, async_session_maker, engine


def _open_mock_json(model: str) -> dict:
    mock_file = f'{settings().TEST_PATH}/mock_data/mock_{model}.json'
    with open(mock_file, 'r', encoding='utf-8') as open_file:
        return json.load(open_file)


def _reformat_data(data: dict) -> dict:
    for d in data:
        d['date_from'] = datetime.strptime(d['date_from'], '%Y-%m-%d')
        d['date_to'] = datetime.strptime(d['date_to'], '%Y-%m-%d')

    return data


@pytest.fixture(scope='session', autouse=True)
async def prepare_database() -> None:
    if settings().MODE != 'TEST':
        raise Exception

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    hotels = _open_mock_json(model='hotels')
    rooms = _open_mock_json(model='rooms')
    users = _open_mock_json(model='users')
    bookings_ = _open_mock_json(model='bookings')

    bookings = _reformat_data(data=bookings_)

    async with async_session_maker() as session:
        add_hotels = insert(base.Hotels).values(hotels)
        add_rooms = insert(base.Rooms).values(rooms)
        add_users = insert(base.Users).values(users)
        add_bookings = insert(base.Bookings).values(bookings)

        await session.execute(add_hotels)
        await session.execute(add_rooms)
        await session.execute(add_users)
        await session.execute(add_bookings)

        await session.commit()


@pytest.fixture(scope='session')
def event_loop(request) -> BaseEventLoop:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='function')
async def async_client() -> AsyncClient:
    async with AsyncClient(app=fastapi_app, base_url='http://test') as async_client:
        yield async_client


@pytest.fixture(scope='function')
async def async_session() -> AsyncSession:
    async with async_session_maker() as async_session:
        yield async_session


@pytest.fixture(scope="session")
async def authenticated_ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        await ac.post(
            '/auth/login',
            json={
                'email': 'test@test.com',
                'password': 'test',
            },
        )
        assert ac.cookies[settings().JWT_TOKEN_NAME]
        yield ac
