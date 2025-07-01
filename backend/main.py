# backend/main.py
from fastapi import FastAPI
from app.routes import router as contacts_router

app = FastAPI()
app.include_router(contacts_router)
