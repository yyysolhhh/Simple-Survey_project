from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from tortoise.backends.base.client import BaseDBAsyncClient

from app.configs.database_settings import connect_db
from app.dtos.participant import ParticipantRequest
from app.routers.welcome import templates
from app.services.participant import get_participant

router = APIRouter()


@router.get("", response_class=HTMLResponse)
def get_form(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="participant.html")


@router.post("")
async def submit_form(data: ParticipantRequest, conn: BaseDBAsyncClient = Depends(connect_db)) -> dict[str, Any]:
    # await get_participant(name=data.name, age=data.age, gender=data.gender)
    participant_id = await get_participant(data, conn)
    return {"redirect": "/questions", "participant_id": participant_id}  # debug url_for
