from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

# from routers import templates
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def welcome(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="index.html")
