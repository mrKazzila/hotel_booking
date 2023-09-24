from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.settings.database import Base


class Users(Base):
    """Model for users."""

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        doc='User email',
        type_=String(100),
        unique=True,
        nullable=False,
    )
    hashed_password: Mapped[str] = mapped_column(
        doc='User password (hash)',
        type_=String(500),
        nullable=False,
    )

    booking: Mapped[list['Bookings']] = relationship(back_populates='user')

    def __str__(self) -> str:
        return f'{self.email}'

    def __repr__(self) -> str:
        return f'{self.email}'
