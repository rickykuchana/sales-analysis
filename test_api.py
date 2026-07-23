from fastapi.testclient import TestClient
from unittest.mock import patch
from api import app

client = TestClient(app)


def test_health():
    """Health endpoint returns 200 and the ok status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_recall():
    """A real campaign number returns the matching recall."""
    response = client.get("/recalls/19V182000")
    assert response.status_code == 200
    assert response.json()["campaign_number"] == "19V182000"


def test_get_recall_not_found():
    """An unknown campaign number returns a 404."""
    response = client.get("/recalls/FAKE123")
    assert response.status_code == 404


def test_get_recall_mocked():
    """Test get_recall without touching the real database."""
    fake_row = ("19V182000", "ACURA", "RDX", 2012, "2019-03-05", "Fake summary text")

    with patch("api.get_connection") as mock_conn:
        mock_cursor = mock_conn.return_value.cursor.return_value
        mock_cursor.fetchone.return_value = fake_row

        response = client.get("/recalls/19V182000")

    assert response.status_code == 200
    assert response.json()["make"] == "ACURA"