from fastapi import APIRouter, Request, Response, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from tortoise.backends.base.client import BaseDBAsyncClient

from app.configs.database_settings import connect_db
from app.routers.welcome import templates
from app.services.question import get_questions

router = APIRouter()


@router.get("", response_class=HTMLResponse)
async def answer(request: Request, conn: BaseDBAsyncClient = Depends(connect_db)) -> Response:
    participant_id = request.cookies.get("participant_id")
    if not participant_id:
        return RedirectResponse("/", status_code=302)
    questions_list = await get_questions()
    return templates.TemplateResponse(request=request, name="question.html", questions=questions_list)
