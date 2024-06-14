from .test_main import client, setup_database

def test_login_user(setup_database):
    response = client.post(
        "/login/",
        json={"password": "password"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Login successful"


def test_invalid_login_user(setup_database):
    response = client.post(
        "/login/",
        json={"password": "wrong password"}
    )
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Invalid credentials"