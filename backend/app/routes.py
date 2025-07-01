# backend/app/routes.py
from fastapi import APIRouter
from app.schemas import Contact

router = APIRouter()

@router.get("/contacts")
def list_contacts():
    return [{"id": 1, "name": "Mario Rossi", "email": "mario@example.com"}]

@router.post("/contacts")
def create_contact(contact: Contact):
    return {"message": "Contatto creato", "data": contact}
