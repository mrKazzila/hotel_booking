from functools import lru_cache
from pathlib import Path
from sys import exit

from pydantic import PostgresDsn, field_validator, UrlConstraints, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class ProjectBaseSettings(BaseSettings):
    __ROOT_DIR_ID: int = 2

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[__ROOT_DIR_ID].joinpath('env/.env'),
    )

    @classmethod
    def _validate_port(cls, v: int) -> int:
        MIN_PORT_NUMBER: int = 1  # noqa
        MAX_PORT_NUMBER: int = 65_535  # noqa

        if MIN_PORT_NUMBER <= v <= MAX_PORT_NUMBER:
            return v
        raise ValueError(f'Port must be between {MIN_PORT_NUMBER} and {MAX_PORT_NUMBER}')


class ProjectSettings(ProjectBaseSettings):
    DOMAIN: str  # TODO: need validate
    DOMAIN_PORT: int

    SECRET_KEY: str
    ALGORITHM: str
    TOKEN_EXPIRE_MIN: int  # TODO: need validate

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str

    field_validator('DOMAIN_PORT', 'SMTP_PORT')(ProjectBaseSettings._validate_port)


class DataBaseSettings(ProjectBaseSettings):
    DB_SCHEME: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    REDIS_HOST: str
    REDIS_PORT: int

    @property
    def database_url(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme=self.DB_SCHEME,
            username=self.DB_USER,
            password=self.DB_PASS,
            host=str(self.DB_HOST),
            port=self.DB_PORT,
            path=f"{self.DB_NAME}",
        )

    field_validator('DB_PORT', 'REDIS_PORT')(ProjectBaseSettings._validate_port)

    @field_validator('DB_SCHEME')
    def __validate_pg_scheme(cls, v: int) -> UrlConstraints.allowed_schemes:
        UrlConstraints.allowed_schemes = ['postgresql+asyncpg']

        if v in UrlConstraints.allowed_schemes:
            return v

        raise ValueError('Invalid PostgresDsn scheme')


class Settings(ProjectSettings, DataBaseSettings):
    STATIC_PATH: str = 'app/static/'


@lru_cache
def settings() -> Settings:
    print(f'Loading settings from env')
    try:
        settings_ = Settings()
        return settings_
    except ValidationError as e:
        exit(e)
