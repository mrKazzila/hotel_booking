from datetime import datetime

from fastapi import Depends, Request
from jose import jwt, JWTError

from app.core.exceptions import (
    ExpireTokenException,
    EmptyTokenException,
    IncorrectTokenFormatException,
    UserNotFoundException,
)
from app.settings.config import settings
from app.users.services import UserServices


def __get_access_token(request: Request):
    if access_token := request.cookies.get('booking_access_token'):  # todo: move to settings
        return access_token

    raise EmptyTokenException


async def get_current_user(access_token: str = Depends(__get_access_token)):
    try:
        payload_data = jwt.decode(
            token=access_token,
            key=settings().SECRET_KEY,
            algorithms=settings().ALGORITHM,
        )
    except JWTError:
        raise IncorrectTokenFormatException

    # TODO: refactor me
    expire_time = payload_data.get('exp')
    if not expire_time or int(expire_time) < int(datetime.utcnow().timestamp()):
        raise ExpireTokenException

    user_id: int = int(payload_data.get('sub'))
    if not user_id:
        raise UserNotFoundException

    if user := await UserServices.find_by_id(model_id=user_id):
        return user

    raise UserNotFoundException
