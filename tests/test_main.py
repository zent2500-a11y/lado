from fastapi.testclient import TestClient

from lado_dashboard.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "라도 대시보드" in response.text
