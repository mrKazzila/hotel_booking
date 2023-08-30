from fastapi import HTTPException, status


class UserNotFoundException(HTTPException):

    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED)


class UserAlreadyExistException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail='User already exist.',
        )


class IncorrectEmailOrPasswordException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect email or password.',
        )


class IncorrectTokenFormatException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect token format.',
        )


class EmptyTokenException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='The token is missing.',
        )


class ExpireTokenException(HTTPException):

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Your token has expired.',
        )
