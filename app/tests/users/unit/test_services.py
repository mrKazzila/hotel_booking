import pytest

from app.tests.users.unit.parametrize_data.services import (
    negative_users_find_by_id_data,
    users_find_by_id_data,
)
from app.users.services import UserServices


@pytest.mark.unit
@pytest.mark.parametrize(
    ['user_id', 'email'],
    users_find_by_id_data,
)
async def test_users_find_by_id(user_id: int, email: str) -> None:
    user = await UserServices.find_by_id(user_id)

    assert user.id == user_id
    assert user.email == email


@pytest.mark.unit
@pytest.mark.parametrize(
    'user_id',
    negative_users_find_by_id_data,
)
async def test_negative_users_find_by_id(user_id: int) -> None:
    user = await UserServices.find_by_id(user_id)
    assert not user
