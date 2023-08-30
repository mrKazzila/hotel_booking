from fastapi import APIRouter, Depends

from app.bookings.schemas import SBooking
from app.bookings.services import BookingServices
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings'],
)


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)) -> SBooking:
    return await BookingServices.find_by_id(model_id=user.id)
