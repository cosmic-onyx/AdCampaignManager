from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

from settings.main_settings import PROJECT_ROOT_PATH


class DataBaseSettings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    @property
    def get_db_url(self):
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT_PATH / '.env',
        extra='allow'
    )


settings = DataBaseSettings()