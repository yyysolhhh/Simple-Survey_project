from fastapi import Depends
from tortoise.backends.base.client import BaseDBAsyncClient

from app.configs.database_settings import connect_db
from app.dtos.participant import ParticipantRequest


async def get_participant(data: ParticipantRequest, conn: BaseDBAsyncClient) -> int:
    sql = "INSERT INTO participants(name, age, gender) VALUES (%s, %s, %s)"  # debug
    participant_id: int = await conn.execute_insert(sql, [data.name, data.age, data.gender])
    return participant_id


# async def get_participant(name: str, age: int, gender: str) -> None:
# participant = Participant(name=name, age=age, gender=gender)
# await participant.save()
# participant = await Participant.create(name=name, age=age, gender=gender)
