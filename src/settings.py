# settings.py

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST")
    POSTGRES_PORT: str = os.environ.get("POSTGRES_PORT")

    DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

