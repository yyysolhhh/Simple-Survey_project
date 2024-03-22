from fastapi import APIRouter

from routers import participant, welcome
# from fastapi.templating import Jinja2Templates
#
# templates = Jinja2Templates(directory="app/templates")
api_router = APIRouter()


api_router.include_router(welcome.router, prefix="")
api_router.include_router(participant.router, prefix="/participants")
