import uvicorn
from fastapi import FastAPI

from app.routers import api_router

app = FastAPI()

app.include_router(api_router, prefix="")
# app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, log_level="debug")
