from datetime import date

from fastapi import APIRouter, Depends

from app.bookings.schemas import SBooking
from app.bookings.services import BookingServices
from app.core.exceptions import RoomCannotBeBookedException, BookingsNotFoundException
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings'],
)


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    if user_bookings := await BookingServices.find_by_id(model_id=user.id):
        return user_bookings

    raise BookingsNotFoundException


@router.post('')
async def add_booking(
        room_id: int,
        date_from: date,
        date_to: date,
        user: Users = Depends(get_current_user),
) -> SBooking:
    if booking := await BookingServices.create_booking(
            user_id=user.id,
            room_id=room_id,
            date_from=date_from,
            date_to=date_to,
    ):
        return booking

    raise RoomCannotBeBookedException
