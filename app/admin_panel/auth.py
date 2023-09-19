from fastapi import status
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from app.core.exceptions import IncorrectEmailOrPasswordException
from app.settings.config import settings
from app.users.auth import authenticate_user, generate_expire_time, create_access_token
from app.users.dependencies import get_current_user


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]

        try:
            if user := await authenticate_user(email=email, password=password):
                expire_time = generate_expire_time(minutes=settings().TOKEN_EXPIRE_MIN)

                access_token = create_access_token(
                    data={'sub': str(user.id)},
                    expire_time=expire_time,
                )
                request.session.update({"token": access_token})
                return True
        except IncorrectEmailOrPasswordException:
            return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> RedirectResponse | bool:
        token = request.session.get("token")

        if not token:
            return RedirectResponse(request.url_for('admin:login'), status_code=status.HTTP_302_FOUND)

        if not (_ := await get_current_user(access_token=token)):
            return RedirectResponse(request.url_for('admin:login'), status_code=status.HTTP_302_FOUND)

        return True


authentication_backend = AdminAuth(secret_key=settings().SECRET_KEY)
