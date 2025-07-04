from pydantic import BaseModel, EmailStr
from typing import Optional

# Schema base: campi comuni
class ContactBase(BaseModel):
    name: str
    email: EmailStr
    phone: str

# Schema per la creazione di un contatto (POST)
class ContactCreate(ContactBase):
    pass

# Schema per l'aggiornamento (PUT/PATCH)
class ContactUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

    model_config = {"from_attributes": True}  # Pydantic v2

# Schema per la risposta (GET)
class Contact(ContactBase):
    id: int

    model_config = {"from_attributes": True}  # Pydantic v2
