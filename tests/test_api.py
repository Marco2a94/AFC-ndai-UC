from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_feedback_valid():
    response = client.post("/feedback", json={
        "campaign_id": "CAMP999",
        "username": "test_user",
        "comment": "Great campaign!",
        "feedback_date": "2025-01-01"
    })
    assert response.status_code == 200

def test_feedback_invalid_payload():
    response = client.post("/feedback", json={
        "campaign_id": "CAMP999"
    })
    assert response.status_code == 422