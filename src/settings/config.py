from pydantic_settings import BaseSettings, SettingsConfigDict

from settings.main_settings import PROJECT_ROOT_PATH


class Settings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_DB: str

    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT_PATH / '.env',
        extra='allow'
    )


settings = Settings()