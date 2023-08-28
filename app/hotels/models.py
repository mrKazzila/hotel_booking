from sqlalchemy import String, SmallInteger
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import mapped_column, Mapped

from app.settings.database import Base


class Hotels(Base):
    __tablename__ = 'hotels'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        name='Hotel name',
        type_=String(60),
        nullable=False,
    )
    location: Mapped[str] = mapped_column(
        name='Hotel location',
        type_=String(500),
        nullable=False,
    )
    services: Mapped[dict] = mapped_column(name='Hotel services', type_=JSONB)
    rooms_quantity: Mapped[int] = mapped_column(name='Rooms quantity')
    image_id: Mapped[int] = mapped_column(name='Hotel image id', type_=SmallInteger)
