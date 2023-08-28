from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from app.settings.database import Base


class Users(Base):
    """Model for users."""

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        doc='User email',
        type_=String(100),
        # unique=True,
        nullable=False,
    )
    hashed_password: Mapped[str] = mapped_column(
        doc='User password (hash)',
        type_=String(500),
        nullable=False,
    )
