from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse

from app.routers.welcome import templates

router = APIRouter()


@router.get("", response_class=HTMLResponse)
def answer(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="quiz.html")
