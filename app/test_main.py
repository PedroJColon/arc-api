from fastapi.testclient import TestClient

from main import read_items
from main import read_selected_item
from main import delete_item
from main import app

client = TestClient(app)

def test_read_items():
    assert read_items()

def test_create_item():
    response = client.post("/items/", json={"id": 3, "name" : "foo", "description": "there goes my hero", "price" : 20, "in_stock": True})
    assert response.json() == {
        "id" : 3,
        "name": "foo",
        "description": "there goes my hero",
        "price": 20,
        "in_stock": True
    }

def test_read_selected_item():
    assert read_selected_item(3)

def test_update():
    response = client.patch("/items/3", json={"id": 3, "name" : "foobar", "description": "there goes my Hero", "price" : 20, "in_stock": False})
    assert response.json() == {
        "id" : 3,
        "name": "foobar",
        "description": "there goes my Hero",
        "price": 20,
        "in_stock": False
    }

def test_delete():
    assert delete_item(3)