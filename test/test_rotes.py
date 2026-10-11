# tests/test_routes.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello FastAPI"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_user():
    response = client.get("/users/7")
    assert response.status_code == 200
    assert response.json() == {
        "id": 7,
        "name": "John Doe",
        "email": "john.doe@example.com",
    }


def test_get_user_invalid_id_returns_422():
    # user_id is declared as int, so FastAPI rejects "abc"
    response = client.get("/users/abc")
    assert response.status_code == 422
