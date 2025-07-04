# backend/app/routes.py
from fastapi import APIRouter, Depends
from app.schemas import Contact, ContactCreate
from sqlalchemy.orm import Session
from .database import get_db
from app import models

router = APIRouter()

@router.get("/contacts", response_model=list[Contact])
def list_contacts(db: Session = Depends(get_db)):
    return db.query(models.Contact).all()

@router.post("/contacts", response_model=Contact)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    db_contact = models.Contact(**contact.model_dump())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


@router.delete("/contacts/{id}", response_model=Contact)
def delete_contact(id: int, db: Session = Depends(get_db)):
    contact = db.query(models.Contact).filter(models.Contact.id == id).first()
    if contact is None:
        raise HTTPException(status_code=404, detail="Contatto non trovato")

    db.delete(contact)
    db.commit()
    return contact

@router.put("/contacts/{id}", response_model=Contact)
def update_contact(id: int, updated: Contact, db: Session = Depends(get_db)):
    contact = db.query(models.Contact).filter(models.Contact.id == id).first()
    if contact is None:
        raise HTTPException(status_code=404, detail="Contatto non trovato")

    contact.name = updated.name
    contact.email = updated.email
    contact.phone = updated.phone

    db.commit()
    db.refresh(contact)
    return contact
