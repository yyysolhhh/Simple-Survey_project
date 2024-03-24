from typing import Any

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse

from app.configs.constants import TEMPLATES
from app.services.question import get_active_questions, get_questions

router = APIRouter()
templates = Jinja2Templates(directory=TEMPLATES)


@router.get("", response_class=HTMLResponse)
async def answer(request: Request) -> Any:
    participant_id = request.cookies.get("participant_id")
    if not participant_id:
        return RedirectResponse("/", status_code=302)
    questions_list = await get_questions()
    return templates.TemplateResponse(request=request, name="question.html", context={"questions": questions_list})


@router.get("/list")
async def show_questions_list() -> JSONResponse:
    questions = await get_active_questions()
    return JSONResponse(content=questions, status_code=200)
