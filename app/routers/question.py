from fastapi import Request, APIRouter, Form
from fastapi.responses import HTMLResponse

from routers.welcome import templates

router = APIRouter()


@router.get("", response_class=HTMLResponse)
def answer(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="quiz.html")
