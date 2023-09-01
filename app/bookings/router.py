from datetime import date

from fastapi import APIRouter, Depends

from app.bookings.schemas import SBooking, SUserBookings
from app.bookings.services import BookingServices
from app.core.exceptions import RoomCannotBeBookedException, BookingsNotFoundException
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings'],
)


@router.get('')
async def get_user_bookings(user: Users = Depends(get_current_user)) -> list[SUserBookings]:
    """Возвращает список всех бронирований пользователя."""
    if user_bookings := await BookingServices.find_all_user_booking(user_id=user.id):
        return user_bookings

    raise BookingsNotFoundException


@router.post('')
async def add_booking(
        room_id: int,
        date_from: date,
        date_to: date,
        user: Users = Depends(get_current_user),
) -> SBooking:
    """Создает бронирование для пользователя."""
    if booking := await BookingServices.create_booking(
            user_id=user.id,
            room_id=room_id,
            date_from=date_from,
            date_to=date_to,
    ):
        return booking

    raise RoomCannotBeBookedException


@router.delete('/{booking_id}')
async def delete_user_booking_by_id(booking_id: int, user: Users = Depends(get_current_user)):
    """Удаляет бронь пользователя."""
    if deleted_book := await BookingServices.delete_user_booking_by_id(booking_id=booking_id, user_id=user.id):
        return deleted_book

    raise BookingsNotFoundException


@router.delete('/')
async def delete_user_bookings(user: Users = Depends(get_current_user)):
    """Удаляет все брони пользователя."""
    if deleted_bookings := await BookingServices.delete_user_bookings(user_id=user.id):
        return deleted_bookings

    raise BookingsNotFoundException
