from app.core.services import BaseServices
from app.rooms.models import Rooms


class RoomsServices(BaseServices):
    model = Rooms
