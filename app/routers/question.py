from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse

from app.routers.welcome import templates
from app.services.question import get_questions

router = APIRouter()


@router.get("", response_class=HTMLResponse)
async def answer(request: Request) -> Response:
    participant_id = request.cookies.get("participant_id")
    if not participant_id:
        return RedirectResponse("/", status_code=302)
    questions_list = await get_questions()
    return templates.TemplateResponse(request=request, name="question.html", questions=questions_list)  # type: ignore
