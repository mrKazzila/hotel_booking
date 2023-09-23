import pytest
from httpx import AsyncClient

from app.users.services import UserServices
from app.tests.users.integration.parametrize_data.routers import register_user_data


@pytest.mark.integration
@pytest.mark.parametrize(
    'email, password, status_code, is_add_in_db',
    register_user_data,
)
async def test_register_user(
        email: str,
        password: str,
        status_code: int,
        is_add_in_db: bool,
        async_client: AsyncClient,
) -> None:
    response = await async_client.post(
        '/auth/register',
        json={
            'email': email,
            'password': password,
        },
    )

    assert response.status_code == status_code

    check_user_in_db = await UserServices.find_one_or_none(email=email)
    is_new_user_in_db = True if check_user_in_db is not None else False

    assert is_new_user_in_db == is_add_in_db
