from fastapi import APIRouter, Depends, Response, status
from fastapi.responses import JSONResponse

from app.core.exceptions import UserAlreadyExistException
from app.settings.config import get_settings as settings
from app.users.auth import authenticate_user, create_access_token, get_password_hash
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
    if _ := not await UserServices.find_one_or_none(email=user_data.email):
        await UserServices.create_user(
            email=user_data.email,
            hashed_password=get_password_hash(password=user_data.password),
        )

    raise UserAlreadyExistException


@router.post('/login')
async def login_user(response: Response, user_data: SUserAuth):
    if user := await authenticate_user(email=user_data.email, password=user_data.password):
        access_token = create_access_token(data={'sub': str(user.id)})

        response.set_cookie(
            key='booking_access_token',
            value=access_token,
            httponly=True,
            expires=settings().TOKEN_EXPIRE_MIN,
        )

        return access_token


@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('booking_access_token')
    return JSONResponse(status_code=status.HTTP_200_OK, content='success logout')


@router.get('/me')
async def get_current_user_info(current_user: Users = Depends(get_current_user)):
    return current_user
