# backend/app/schemas.py
from pydantic import BaseModel, EmailStr


class Contact(BaseModel):
    id: int | None = None
    name: str
    email: EmailStr
    phone: str
