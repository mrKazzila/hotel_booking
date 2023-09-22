from pydantic import BaseModel, EmailStr, field_validator


class SUserAuth(BaseModel):
    email: EmailStr
    password: str

    @field_validator('password')
    def __validate_password_length(cls, v: str) -> str:
        password_len = len(v)

        if any([
            password_len < 3,
            v is None,
            v.count(' ') > 0,  # whitespace
        ]):
            raise ValueError('Password is empty or less then 5')

        return v
