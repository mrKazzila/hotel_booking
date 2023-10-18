import logging
from functools import lru_cache
from pathlib import Path
from sys import exit
from typing import Annotated, Literal

from annotated_types import Ge, Le, MinLen
from pydantic import HttpUrl, PostgresDsn, SecretStr, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)


class ProjectBaseSettings(BaseSettings):
    __ROOT_DIR_ID: int = 2

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[__ROOT_DIR_ID].joinpath('env/.env'),
    )


class ProjectSettings(ProjectBaseSettings):
    MODE: Literal['DEV', 'TEST', 'PROD']

    SENTRY_URL: HttpUrl
    TRACES_SAMPLE_RATE: float
    PROFILES_SAMPLE_RATE: float

    DOMAIN: str  # TODO: need validate
    DOMAIN_PORT: Annotated[int, Ge(1), Le(65_535)]

    SECRET_KEY: str
    ALGORITHM: str
    TOKEN_EXPIRE_MIN: Annotated[int, Ge(30)]

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str


class DatabaseSettings(ProjectBaseSettings):
    DB_SCHEME: str
    DB_HOST: str
    DB_PORT: Annotated[int, Ge(1), Le(65_535)]
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    TEST_DB_SCHEME: str
    TEST_DB_HOST: str
    TEST_DB_PORT: Annotated[int, Ge(1), Le(65_535)]
    TEST_DB_USER: str
    TEST_DB_PASS: Annotated[SecretStr, MinLen(8)]
    TEST_DB_NAME: str

    REDIS_HOST: str
    REDIS_PORT: Annotated[int, Ge(1), Le(65_535)]

    @property
    def database_url(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme=self.DB_SCHEME,
            username=self.DB_USER,
            password=self.DB_PASS,
            host=str(self.DB_HOST),
            port=self.DB_PORT,
            path=f'{self.DB_NAME}',
        )

    @property
    def test_database_url(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme=self.TEST_DB_SCHEME,
            username=self.TEST_DB_USER,
            password=self.TEST_DB_PASS,
            host=str(self.TEST_DB_HOST),
            port=self.TEST_DB_PORT,
            path=f'{self.TEST_DB_NAME}',
        )


class Settings(ProjectSettings, DatabaseSettings):
    STATIC_PATH: str = 'app/static/'
    TEST_PATH: str = 'app/tests/'
    TEMPLATES_PATH: str = 'app/templates'
    JWT_TOKEN_NAME: str = 'booking_access_token'


@lru_cache
def settings() -> Settings:
    logger.info('Loading settings from env')
    try:
        settings_ = Settings()
        return settings_

    except ValidationError as e:
        logger.error('Error at loading settings from env. %(err)s', {'err': e})
        exit(e)
