from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.settings.database import Base


class Rooms(Base):
    """Model for rooms."""

    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003
    hotel_id: Mapped[str] = mapped_column(ForeignKey('hotels.id'), nullable=False)

    name: Mapped[str] = mapped_column(
        doc='Room name',
        type_=String(100),
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        doc='Room description',
        type_=String(3000),
        nullable=True,
    )
    price: Mapped[int] = mapped_column(
        doc='Room price',
        type_=Integer,
        nullable=False,
    )
    services: Mapped[dict] = mapped_column(
        doc='Room services',
        type_=JSONB,
        nullable=True,
    )
    quantity: Mapped[int] = mapped_column(
        doc='Number of rooms',
        type_=Integer,
        nullable=False,
    )
    image_id: Mapped[int] = mapped_column(
        doc='Room image id',
        type_=Integer,
    )

    hotel: Mapped['Hotels'] = relationship(back_populates='rooms')
    bookings: Mapped[list['Bookings']] = relationship(back_populates='room')

    def __str__(self) -> str:
        return f'{self.name}'
