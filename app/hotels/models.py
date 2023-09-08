from sqlalchemy import String, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import mapped_column, Mapped

from app.settings.database import Base


class Hotels(Base):
    """Model for hotels."""

    __tablename__ = 'hotels'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        doc='Hotel name',
        type_=String(60),
        nullable=False,
    )
    location: Mapped[str] = mapped_column(
        doc='Hotel location',
        type_=String(500),
        nullable=False,
    )
    services: Mapped[dict] = mapped_column(
        doc='Hotel services',
        type_=JSONB,
    )
    rooms_quantity: Mapped[int] = mapped_column(
        doc='Number of hotel rooms',
        type_=Integer,
    )
    image_id: Mapped[int] = mapped_column(
        doc='Hotel image id',
        type_=Integer,
    )
