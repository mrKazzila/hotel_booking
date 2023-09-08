from fastapi import APIRouter

from app.core.exceptions import RoomsNotFoundException
from app.rooms.services import RoomsServices

router = APIRouter(
    prefix='/rooms',
    tags=['Rooms']
)


@router.get('/{hotel_id}')
async def get_rooms_from_hotel(hotel_id: int):
    if hotel_rooms := await RoomsServices.find_one_or_none(id=hotel_id):
        return hotel_rooms

    raise RoomsNotFoundException
