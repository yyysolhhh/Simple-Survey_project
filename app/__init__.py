from fastapi import FastAPI

from app.configs import Settings
from app.routers import api_router

app = FastAPI()


app.include_router(api_router, prefix=Settings.API_V1_STR)
