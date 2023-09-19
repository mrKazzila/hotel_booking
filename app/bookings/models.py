from datetime import date

from sqlalchemy import Date, Computed, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.settings.database import Base


class Bookings(Base):
    """Model for bookings."""

    __tablename__ = 'bookings'

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    date_from: Mapped[date] = mapped_column(
        doc='Booking from date',
        type_=Date,
        nullable=False,
    )
    date_to: Mapped[date] = mapped_column(
        doc='Booking date to',
        type_=Date,
        nullable=False,
    )
    price: Mapped[int] = mapped_column(
        doc='Booking price',
        type_=Integer,
        nullable=False,
    )
    total_cost: Mapped[int] = mapped_column(
        Computed('(date_to - date_from) * price'),
        doc='Total booking cost',
        type_=Integer,
    )
    total_days: Mapped[int] = mapped_column(
        Computed('date_to - date_from'),
        doc='Booking day count',
        type_=Integer,
    )

    user = relationship('Users', back_populates='booking')
    room = relationship('Rooms', back_populates='bookings')

    def __str__(self):
        return f'Booking №{self.id}'
