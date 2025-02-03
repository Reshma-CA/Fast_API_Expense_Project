from fastapi import FastAPI
import models
from database import engine
from routes import router

app = FastAPI()

# Create Database Tables
models.Base.metadata.create_all(bind=engine)

# Include Router
app.include_router(router)