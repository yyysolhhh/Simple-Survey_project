from typing import Any

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from tortoise.backends.base.client import BaseDBAsyncClient

# from app import app
from app.configs.constants import TEMPLATES
from app.configs.database_settings import connect_db
from app.dtos.participant import ParticipantRequest
from app.services.participant import get_participant

router = APIRouter()
templates = Jinja2Templates(directory=TEMPLATES)


@router.get("", response_class=HTMLResponse)
def get_form(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="participant.html")


@router.post("")
async def submit_form(
    request: Request, data: ParticipantRequest, conn: BaseDBAsyncClient = Depends(connect_db)
) -> dict[str, Any]:
    # participant_id = await Participant.create(name=data.name, age=data.age, gender=data.gender)
    participant_id = await get_participant(data, conn)
    return {"redirect": "/api/v1/questions", "participant_id": participant_id}  # debug url_for
    # return {"redirect": router.url_path_for("routers.question.answer"), "participant_id": participant_id}  # debug url_for
    # return {"redirect": request.url_for("answer"), "participant_id": participant_id}  # debug url_for
