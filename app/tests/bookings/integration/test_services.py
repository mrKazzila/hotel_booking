from datetime import datetime

import pytest

from app.bookings.services import BookingServices
from app.tests.bookings.integration.parametrize_data.services import add_and_get_booking_data


@pytest.mark.parametrize(
    'user_id, room_id, date_from, date_to',
    add_and_get_booking_data,
)
async def test_add_and_get_booking(
        user_id: int,
        room_id: int,
        date_from: datetime,
        date_to: datetime,
) -> None:
    new_booking = await BookingServices.create_booking(
        user_id=user_id,
        room_id=room_id,
        date_from=date_from,
        date_to=date_to,
    )

    assert new_booking.user_id == user_id
    assert new_booking.room_id == room_id

    new_booking_exist = await BookingServices.find_by_id(new_booking.id)
    assert new_booking_exist is not None
