import os
from dotenv import load_dotenv

from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    DB_HOST: str = os.getenv('DB_HOST')
    DB_PORT: str = os.getenv("DB_PORT")
    DB_USER: str = os.getenv("DB_USER")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_PASS: str = os.getenv("DB_PASS")
    SQL_DATABASE_URL: str = (f"postgresql://{DB_USER}:"
                             f"{DB_PASS}@{DB_HOST}:"
                             f"{DB_PORT}/{DB_NAME}")

    print(f"Загруженные настройки проекта:\n1) База данных - {SQL_DATABASE_URL.split(":")[0]}\n2) URL базы данных - {SQL_DATABASE_URL}")


settings = Settings()