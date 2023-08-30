from app.core.services import BaseServices
from app.users.models import Users


class UserServices(BaseServices):
    model = Users

    @classmethod
    async def create_user(cls, **data):
        return await super().add_entity(**data)
