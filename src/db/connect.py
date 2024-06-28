# core/connect.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

SQLALCHEMY_URL = settings.POSTGRES_PATH

engine = create_engine(SQLALCHEMY_URL, echo=False, pool_size=5, max_overflow=0)
DBSession = sessionmaker(bind=engine, expire_on_commit=False)


def get_db():
    '''
    The function get_db to use as depended for get session to work with DB

    Returns:
    Session to work with DB  
    
    '''
    db = DBSession()
    try:
        yield db
    except Exception as e:
       print(e)
    finally:
        db.close()
