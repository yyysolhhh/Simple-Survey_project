from __future__ import annotations

from tortoise import fields
from tortoise.models import Model

from app.models.base_model import BaseModel


class Question(BaseModel, Model):
    order = fields.IntField(default=0)
    is_active = fields.BooleanField(default=True)
    content = fields.TextField()

    class Meta:
        table = "questions"

    @classmethod
    async def get_all_questions(cls) -> list[Question]:
        return await cls.all()

    @classmethod
    async def get_all_active_questions(cls) -> list[Question]:
        return await cls.filter(is_active=True).order_by("order").all()

    @classmethod
    async def get_question_by_id(cls, question_id: int) -> Question:
        return await cls.filter(id=question_id).first()
