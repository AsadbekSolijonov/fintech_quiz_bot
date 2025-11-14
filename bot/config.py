import os.path
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

abs_path = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.join(abs_path, '.env')


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR,
        env_file_encoding='utf-8',
        extra='ignore'
    )

    BOT_TOKEN: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str


settings = Settings()
if __name__ == '__main__':
    print(settings.DB_NAME)
    print(settings.DB_PORT)
    print(settings.DB_HOST)
    print(settings.DB_PASSWORD)
    print(settings.DB_USER)
    print(settings.BOT_TOKEN)
