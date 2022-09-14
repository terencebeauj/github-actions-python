"""Test for the API endpoints
"""

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_read_main():
    """Test for the root endpoint
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "Ok"}

def test_get_prediction():
    """Test the prediction endpoint
    """
    response = client.get("/prediction/btcbusd")
    assert response.status_code == 200
    assert isinstance(response.json()["prediction"], float)
