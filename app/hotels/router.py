from fastapi import APIRouter

from app.core.exceptions import HotelNotFoundException
from app.hotels.services import HotelServices
from app.hotels.schemas import SHotelInfo

router = APIRouter(
    prefix='/hotels',
    tags=['Hotels']
)


@router.get('/')
async def get_hotels() -> list[SHotelInfo]:
    if hotels := await HotelServices.find_all():
        print(list(hotels))
        return hotels

    raise HotelNotFoundException


@router.get('/id/{hotel_id}')
async def get_hotel_info(hotel_id: int) -> SHotelInfo:
    if hotel_info := await HotelServices.find_one_or_none(id=hotel_id):
        return hotel_info

    raise HotelNotFoundException
