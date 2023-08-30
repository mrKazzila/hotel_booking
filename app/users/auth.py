from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.core.exceptions import IncorrectEmailOrPasswordException
from app.settings.config import get_settings as settings
from app.users.services import UserServices

pwd_context = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto',
)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(secret=password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(secret=plain_password, hash=hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire_time = datetime.utcnow() + timedelta(minutes=settings().TOKEN_EXPIRE_MIN)

    to_encode.update({'exp': expire_time})
    encode_jwt = jwt.encode(
        claims=to_encode,
        key=settings().SECRET_KEY,
        algorithm=settings().ALGORITHM,
    )

    return encode_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UserServices.find_one_or_none(email=email)

    if user and verify_password(plain_password=password, hashed_password=user.hashed_password):
        return user

    raise IncorrectEmailOrPasswordException
