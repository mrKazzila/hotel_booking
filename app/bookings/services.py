from app.bookings.models import Bookings
from app.core.services import BaseServices


class BookingServices(BaseServices):
    model = Bookings
