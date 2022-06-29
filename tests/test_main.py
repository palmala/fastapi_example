from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}


def test_add():
    response = client.get("/add/1/1")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "result": "2"}

    response = client.get("/add/1/-1")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "result": "0"}
