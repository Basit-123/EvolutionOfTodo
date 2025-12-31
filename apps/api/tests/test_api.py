from fastapi.testclient import TestClient
from ..src.main import app, engine
from sqlmodel import SQLModel

# Create tables for testing
SQLModel.metadata.create_all(engine)

client = TestClient(app)

def test_read_todos():
    response = client.get("/api/v1/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_todo():
    payload = {
        "title": "Test API Todo",
        "description": "Verification",
        "priority": "high",
        "tags": "[]"
    }
    response = client.post("/api/v1/todos", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Test API Todo"
