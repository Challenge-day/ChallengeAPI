from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from pydantic import PostgresDsn

from settings.settings import Settings

settings = Settings()

def build_db_connection_url(custom_db: Optional[str] = None):
    db_name = f"/{settings.POSTGRES_DB or ''}" if custom_db is None else "/" + custom_db
    return PostgresDsn.build(
        scheme='postgresql+psycopg2',
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        host=settings.POSTGRES_HOST,
        path=db_name,
    )


def create_database(db_name: str):
    try:
        eng = create_engine(build_db_connection_url(custom_db=db_name))
        conn = eng.connect()
        conn.close()
    except OperationalError as exc:
        if "does not exist" in exc.__str__():
            eng = create_engine(build_db_connection_url(custom_db="postgres"))
            conn = eng.connect()
            conn.execute("commit")
            conn.execute(f"create database {db_name}")
            conn.close()
            print(f"Database {db_name} created")
        else:
            raise exc
    eng.dispose()

create_database("test_database")