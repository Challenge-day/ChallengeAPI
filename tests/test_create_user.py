from .test_main import client, setup_database

def test_create_user(setup_database):
    response = client.post(
        "/users/",
        json={"username": "testuser", "email": "test@example.com", "password": "password", "telegram_id": 123456, "first_name": "Test", "language_code": "en"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"