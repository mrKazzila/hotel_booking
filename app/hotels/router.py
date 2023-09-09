import asyncio

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.core.exceptions import HotelNotFoundException
from app.hotels.schemas import SHotelInfo
from app.hotels.services import HotelServices

router = APIRouter(
    prefix='/hotels',
    tags=['Hotels']
)


@router.get('/')
@cache(expire=60)
async def get_hotels() -> list[SHotelInfo]:
    if hotels := await HotelServices.find_all():
        await asyncio.sleep(5)  # for cache example
        return hotels

    raise HotelNotFoundException


@router.get('/id/{hotel_id}')
async def get_hotel_info(hotel_id: int) -> SHotelInfo:
    if hotel_info := await HotelServices.find_one_or_none(id=hotel_id):
        return hotel_info

    raise HotelNotFoundException
