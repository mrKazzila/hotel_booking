from sqladmin import ModelView

from app.bookings.models import Bookings
from app.hotels.models import Hotels
from app.rooms.models import Rooms
from app.users.models import Users


class UsersAdmin(ModelView, model=Users):
    name = 'User'
    name_plural = 'Users'
    icon = 'fa-solid fa-user'
    can_delete = False

    column_list = [Users.id, Users.email, Users.booking]
    column_formatters = {Users.booking: lambda m, a: m.booking[:10]}
    column_sortable_list = [Users.id]
    column_details_exclude_list = [Users.hashed_password]

    page_size = 20
    page_size_options = [25, 50, 100]


class BookingsAdmin(ModelView, model=Bookings):
    name = 'Booking'
    name_plural = 'Bookings'
    icon = 'fa-solid fa-book'

    column_list = '__all__'
    column_sortable_list = [
        Bookings.id,
        Bookings.date_from,
        Bookings.date_to,
        Bookings.price,
    ]

    page_size = 10
    page_size_options = [20, 40, 100]


class RoomsAdmin(ModelView, model=Rooms):
    name = 'Room'
    name_plural = 'Rooms'
    icon = 'fa-solid fa-bed'

    column_list = [
        Rooms.id,
        Rooms.hotel,
        Rooms.name,
        Rooms.price,
        Rooms.quantity,
        Rooms.bookings,
    ]
    column_sortable_list = [Rooms.id, Rooms.name, Rooms.price, Rooms.quantity]

    page_size = 10
    page_size_options = [20, 40, 100]


class HotelsAdmin(ModelView, model=Hotels):
    name = 'Hotel'
    name_plural = 'Hotels'
    icon = 'fa-solid fa-hotel'

    column_list = [
        Hotels.id,
        Hotels.name,
        Hotels.rooms_quantity,
        Hotels.rooms,
        Hotels.location,
    ]
    column_sortable_list = [Hotels.id, Hotels.name, Hotels.rooms_quantity]

    page_size = 10
    page_size_options = [20, 40, 100]
