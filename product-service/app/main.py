from fastapi import FastAPI
from . import models
from .database import engine
from .routes import router

app = FastAPI(title="Product Service")
models.Base.metadata.create_all(bind=engine)

app.include_router(router)
