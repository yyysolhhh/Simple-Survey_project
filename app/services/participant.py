from tortoise.backends.base.client import BaseDBAsyncClient

from app.dtos.participant import ParticipantRequest
from app.models.participant import Participant


async def get_participant(data: ParticipantRequest, conn: BaseDBAsyncClient) -> int:
    participant_id = await Participant.insert_participant(conn, data)
    return participant_id
