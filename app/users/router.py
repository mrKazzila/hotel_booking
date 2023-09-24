from fastapi import APIRouter, Depends, Response, status
from fastapi.responses import JSONResponse

from app.core.exceptions import UserAlreadyExistException
from app.settings.config import settings
from app.users.auth import (
    authenticate_user,
    create_access_token,
    generate_expire_time,
    get_password_hash,
)
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.schemas import SUserAuth
from app.users.services import UserServices

router = APIRouter(
    prefix='/auth',
    tags=['Auth & Users'],
)


@router.post('/register')
async def register_user(user_data: SUserAuth):
    user_exists = await UserServices.find_one_or_none(email=user_data.email)

    if user_exists:
        raise UserAlreadyExistException

    await UserServices.create_user(
        email=user_data.email,
        hashed_password=get_password_hash(password=user_data.password),
    )


@router.post('/login')
async def login_user(response: Response, user_data: SUserAuth):
    if user := await authenticate_user(
        email=user_data.email,
        password=user_data.password,
    ):
        expire_time = generate_expire_time(minutes=settings().TOKEN_EXPIRE_MIN)

        access_token = create_access_token(
            data={'sub': str(user.id)},
            expire_time=expire_time,
        )

        response.set_cookie(
            key=settings().JWT_TOKEN_NAME,
            value=access_token,
            httponly=True,
            expires=expire_time,
        )

        return access_token


@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie(settings().JWT_TOKEN_NAME)
    return JSONResponse(status_code=status.HTTP_200_OK, content='success logout')


@router.get('/me')
async def get_current_user_info(current_user: Users = Depends(get_current_user)):
    return current_user
