from datetime import date

from sqlalchemy import select, func, insert

from app.bookings.models import Bookings
from app.core.services import BaseServices
from app.hotels.models import Rooms
from app.settings.database import async_session_maker


class BookingServices(BaseServices):
    model = Bookings

    @classmethod
    async def create_booking(cls, user_id: int, room_id: int, date_from: date, date_to: date):
        #
        """
        ROW SQL EXAMPLE
            with booked_rooms as (
                select * from bookings
                where room_id = 1 and
                (date_from >= '2033-05-15' and date_from <= '2033-06-20') or
                (date_from <= '2033-05-15' and date_to > '2033-05-15')
            )
            select rooms.quantity - COUNT(booked_rooms.room_id) from rooms
            left join booked_rooms on booked_rooms.room_id = rooms.id
            where rooms.id = 1
            group by rooms.quantity, booked_rooms.room_id;
        """
        # TODO refactor me
        booked_rooms_query = (
            select(Bookings)
            .where(
                (Bookings.room_id == room_id) &
                (
                        ((Bookings.date_from >= date_from) & (Bookings.date_from <= date_to)) |
                        ((Bookings.date_from <= date_from) & (Bookings.date_to > date_from))
                )
            )
        ).cte('booked_rooms')

        rooms_left_query = (
            select((Rooms.quantity - func.count(booked_rooms_query.c.room_id)).label('rooms_left'))
            .select_from(Rooms).join(booked_rooms_query, booked_rooms_query.c.room_id == Rooms.id, isouter=True)
            .where(Rooms.id == room_id)
            .group_by(Rooms.quantity, booked_rooms_query.c.room_id)
        )

        async with async_session_maker() as session:
            rooms_left = await session.execute(rooms_left_query)
            get_rooms_left: int = rooms_left.scalar()

            if get_rooms_left > 0:
                get_room_price_query = (
                    select(Rooms.price)
                    .filter_by(id=room_id)
                )

                get_room_price = await session.execute(get_room_price_query)
                room_price: int = get_room_price.scalar()

                add_booking = (
                    insert(Bookings)
                    .values(
                        room_id=room_id,
                        user_id=user_id,
                        date_from=date_from,
                        date_to=date_to,
                        price=room_price,
                    )
                ).returning(Bookings)

                new_booking = await session.execute(add_booking)
                await session.commit()

                return new_booking.scalar()
            else:
                return None
