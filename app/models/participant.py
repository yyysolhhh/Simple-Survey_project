from __future__ import annotations

from tortoise import fields
from tortoise.backends.base.client import BaseDBAsyncClient
from tortoise.models import Model

from app.dtos.participant import ParticipantRequest
from app.models.base_model import BaseModel


class Participant(BaseModel, Model):
    name = fields.CharField(max_length=10)
    age = fields.IntField()
    gender = fields.CharField(max_length=10, default="other")

    class Meta:
        table = "participants"

    @classmethod
    async def get_one_by_id(cls, id: int) -> Participant:
        return await cls.get(id=id)

    @classmethod
    async def get_all_participants(cls) -> list[Participant]:
        return await cls.all()

    @classmethod
    async def insert_participant(cls, conn: BaseDBAsyncClient, data: ParticipantRequest) -> int:
        sql = "INSERT INTO participants(name, age, gender) VALUES (%s, %s, %s)"  # debug
        participant_id: int = await conn.execute_insert(sql, [data.name, data.age, data.gender])
        return participant_id
