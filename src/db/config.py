# core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings():

    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DOMAIN = os.getenv('POSTGRES_DOMAIN')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT')
    POSTGRES_DB = os.getenv('POSTGRES_DB')
    POSTGRES_PATH = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_DOMAIN}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()

