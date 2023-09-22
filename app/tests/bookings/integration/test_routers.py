import pytest
from httpx import AsyncClient

from app.tests.bookings.integration.parametrize_data import (
    router_add_and_get_booking_data,
    router_delete_user_booking_by_id_data,
)


@pytest.mark.parametrize(
    'room_id, date_from, date_to, book_count, status_code',
    router_add_and_get_booking_data,
)
async def test_add_and_get_booking(
        room_id: int,
        date_from: str,
        date_to: str,
        book_count: int,
        status_code: int,
        authenticated_ac: AsyncClient,
) -> None:
    response = await authenticated_ac.post(
        '/bookings',
        json={
            'room_id': room_id,
            'date_from': date_from,
            'date_to': date_to,
        },
    )

    assert response.status_code == status_code

    response_ = await authenticated_ac.get('/bookings')
    assert len(response_.json()) == book_count


@pytest.mark.parametrize(
    'booking_id, status_code',
    router_delete_user_booking_by_id_data,
)
async def test_delete_user_booking_by_id(booking_id, status_code, authenticated_ac: AsyncClient):
    response = await authenticated_ac.delete(
        '/bookings/',
        params={'booking_id': booking_id},
    )

    assert response.status_code == status_code

    response_ = await authenticated_ac.get('/bookings')
    assert response_.json() == {'detail': 'Bookings not found.'}
