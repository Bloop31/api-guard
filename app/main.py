from fastapi import FastAPI
from app.routes import users
from app.database import engine
from app import models


app=FastAPI(title="API Guard System")
models.Base.metadata.create_all(bind=engine)
app.include_router(users.router)