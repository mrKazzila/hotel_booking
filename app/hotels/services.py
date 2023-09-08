from app.core.services import BaseServices
from app.hotels.models import Hotels


class HotelServices(BaseServices):
    model = Hotels
