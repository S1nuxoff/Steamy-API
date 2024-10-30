# app/main.py
import uvicorn
from fastapi import FastAPI

from app.core.config import settings
from app.api.v1.api import api_router
from app.middleware.logging_middleware import LoggingMiddleware
from app.db.base import create_all_tables

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
)

app.add_middleware(LoggingMiddleware)

app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
async def on_startup():
    await create_all_tables()
    print("Database initialized.")

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
