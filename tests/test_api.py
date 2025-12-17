
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue dans mon API FastAPI !"}

def test_read_item():
    response = client.get("/items/1?q=test")
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 1
    assert data["query"] == "test"

def test_create_item():
    payload = {"name": "Laptop", "price": 999.99, "in_stock": True}
    response = client.post("/items/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["item"]["name"] == "Laptop"
    assert data["item"]["price"] == 999.99
    assert data
