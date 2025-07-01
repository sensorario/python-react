# backend/app/routes.py
from fastapi import APIRouter

from app.schemas import Contact

router = APIRouter()

# Memoria temporanea
contacts: list[Contact] = []
id_counter = 1


@router.get("/contacts")
def list_contacts() -> list[Contact]:
    return contacts


@router.post("/contacts")
def create_contact(contact: Contact) -> Contact:
    global id_counter
    contact.id = id_counter
    contacts.append(contact)
    id_counter += 1
    return contact
