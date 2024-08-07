from fastapi.testclient import TestClient
from app.unitario import app

client = TestClient(app)

def test_unitario():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
