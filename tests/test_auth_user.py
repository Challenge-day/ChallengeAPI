import pytest
# import pytest_asyncio
# from httpx import AsyncClient
from fastapi.testclient import TestClient

from main import app
from src.db.connect import get_db
from src.models.entity import Base
from tests.test_main import engine, override_get_db

Base.metadata.create_all(bind=engine)
app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client

def test_create_auth(client):
    response = client.post("/auth", json={"username": "testuser", "telegram_id": 123456})
    assert response.status_code == 200

def test_get_auth(client):
    # Сначала создаем запись
    client.post("/auth", json={"username": "testuser", "telegram_id": 123456})
    # Затем получаем ее
    response = client.get("/auth/123456")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["telegram_id"] == 123456

def test_get_auth_not_found(client):
    response = client.get("/auth/999999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Not Found"
