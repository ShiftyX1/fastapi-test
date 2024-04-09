import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    SQL_DATABASE_URL: str = "sqlite:///test.db"


    print(f"Загруженные настройки проекта:\n1) База данных - {SQL_DATABASE_URL.split(":")[0]}\n2) URL базы данных - {SQL_DATABASE_URL}")


settings = Settings()