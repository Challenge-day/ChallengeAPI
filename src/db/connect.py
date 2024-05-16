# core/connect.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

POSTGRES_URI = settings.POSTGRES_PATH

engine = create_engine(POSTGRES_URI, echo=False, pool_size=5, max_overflow=0)
DBSession = sessionmaker(bind=engine)


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
