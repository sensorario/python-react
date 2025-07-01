from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_and_get_contact() -> None:
    contact = {"name": "Alice", "email": "alice@example.com", "phone": "1234567890"}

    # Test POST
    response = client.post("/contacts", json=contact)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == contact["name"]
    assert data["email"] == contact["email"]
    assert data["phone"] == contact["phone"]
    assert "id" in data

    # Test GET
    response = client.get("/contacts")
    assert response.status_code == 200
    contacts = response.json()
    assert any(c["email"] == "alice@example.com" for c in contacts)
