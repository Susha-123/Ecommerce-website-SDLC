from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Mock Payment Service")

app.include_router(router)
