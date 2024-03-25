from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from tortoise.backends.base.client import BaseDBAsyncClient

from app.configs.constants import TEMPLATES
from app.configs.database_settings import connect_db
from app.services.answer import collect_answers

router = APIRouter()
templates = Jinja2Templates(directory=TEMPLATES)


@router.get("/")
def login(request: Request):
    username = request.query_params.get("username")



@router.get("/dashboard", response_class=HTMLResponse)
def get_dashboard_page(request: Request):
    pass
    # graph_div =
    # return templates.TemplateResponse(request=request, name="dashboard.html", context={"graph_div": graph_div})