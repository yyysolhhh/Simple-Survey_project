from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse

# import templates
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

from app.routers.welcome import templates
from app.services.question import get_questions

# from app.services.question import get_questions
#
# templates = Jinja2Templates(directory="app/templates")

router = APIRouter()


@router.get("", response_class=HTMLResponse)
async def answer(request: Request) -> Response | _TemplateResponse:
    participant_id = request.cookies.get("participant_id")
    if not participant_id:
        return RedirectResponse("/", status_code=302)
    questions_list = await get_questions()
    return templates.TemplateResponse(request=request, name="question.html", context={"question_list": questions_list})
