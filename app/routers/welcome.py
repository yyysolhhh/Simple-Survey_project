from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.configs.constants import TEMPLATES

templates = Jinja2Templates(directory=TEMPLATES)


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def welcome(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="index.html")
