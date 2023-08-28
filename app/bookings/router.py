from fastapi import APIRouter

from app.bookings.schemas import SBooking
from app.bookings.services import BookingServices

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings'],
)


@router.get('')
async def get_bookings() -> SBooking:
    return await BookingServices.find_all()
