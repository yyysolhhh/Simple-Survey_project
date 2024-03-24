from __future__ import annotations

from tortoise import fields
from tortoise.models import Model

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
