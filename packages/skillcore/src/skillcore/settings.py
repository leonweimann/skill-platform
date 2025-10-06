from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

Env = Literal["dev", "stating", "prod"]


class BaseAppSettings(BaseSettings):
    env: Env = "dev"
    database_url: str = "..."  # TODO: To be set later
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "DEBUG"

    clockodo_token: str | None = None
    sevdesk_token: str | None = None
    discord_token: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


class ApiSettings(BaseAppSettings):
    http_host: str = "0.0.0.0"
    http_port: int = 8000


class WorkerSettings(BaseAppSettings):
    timezone: str = "Europe/Berlin"


class BotSettings(BaseAppSettings):
    pass
