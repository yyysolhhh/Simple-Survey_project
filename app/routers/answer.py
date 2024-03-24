from fastapi import APIRouter, Depends, Request
from starlette.responses import JSONResponse
from tortoise.backends.base.client import BaseDBAsyncClient

from app.configs.database_settings import connect_db
from app.services.answer import collect_answers

router = APIRouter()


@router.post("")
async def submit_answers(request: Request, conn: BaseDBAsyncClient = Depends(connect_db)) -> JSONResponse:
    participant_id: str | None = request.cookies.get("participant_id")
    if not participant_id:
        return JSONResponse({"error": "Participant ID not found"}, status_code=400)
    data = await request.json()
    await collect_answers(data, participant_id, conn)
    return JSONResponse(
        {
            "message": "Answers submitted.",
            "redirect": "/results",
        }
    )
