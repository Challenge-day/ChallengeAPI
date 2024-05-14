# core/connect.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

POSTGRES_URL = settings.POSTGRES_PATH

engine = create_engine(POSTGRES_URL, echo=False, max_overflow=5)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    '''
    The function get_db to use as depended for get session to work with DB

    Returns:
    Session to work with DB  
    
    '''
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
       print(e)
    finally:
        db.close()