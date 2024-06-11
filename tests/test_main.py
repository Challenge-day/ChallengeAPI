import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
from models.entity import Base
from src.db.config import settings
from src.db.connect import get_db


SQLALCHEMY_URL = settings.POSTGRES_PATH

engine = create_engine(SQLALCHEMY_URL, echo=False, pool_size=5, max_overflow=0)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
DBSession = sessionmaker(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    yield
    Base.metadata.drop_all(bind=engine) 


