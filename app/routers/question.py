from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse

from app.routers.welcome import templates

router = APIRouter()


@router.get("", response_class=HTMLResponse)
def answer(request: Request) -> Response:
    participant_id = request.cookies.get("participant_id")
    if not participant_id:
        return RedirectResponse("/", status_code=302)

    return templates.TemplateResponse(request=request, name="question.html")
