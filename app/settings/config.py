from functools import lru_cache
from pathlib import Path
from sys import exit

from pydantic import PostgresDsn, field_validator, UrlConstraints, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_SCHEME: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

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

    @field_validator('DB_PORT')
    def __validate_port(cls, v: int) -> int:
        if not 1 <= v <= 65_535:
            raise ValueError("Port must be between 1 and 65535")
        return v

    @field_validator('DB_SCHEME')
    def __validate_pg_scheme(cls, v: int) -> UrlConstraints.allowed_schemes:
        UrlConstraints.allowed_schemes = ['postgresql+asyncpg']

        if v not in UrlConstraints.allowed_schemes:
            raise ValueError('Invalid PostgresDsn scheme')

        return v

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[2].joinpath('env/.env'),
    )


@lru_cache
def get_settings() -> Settings:
    print(f'Loading settings from env')
    try:
        settings = Settings()
        return settings
    except ValidationError as e:
        exit(e)
