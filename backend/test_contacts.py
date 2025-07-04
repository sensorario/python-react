import random
import string
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_and_get_contact() -> None:
    random_email = (
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))
        + "@example.com"
    )
    contact = {"name": "Alice", "email": random_email, "phone": "1234567890"}

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
    assert any(c["email"] == random_email for c in contacts)
