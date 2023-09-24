# Import all the models, so that Base has them before being
# imported by Alembic
from app.bookings.models import Bookings  # noqa
from app.hotels.models import Hotels  # noqa
from app.rooms.models import Rooms  # noqa
from app.settings.database import Base  # noqa
from app.users.models import Users  # noqa
