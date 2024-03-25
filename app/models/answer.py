from __future__ import annotations

from typing import Any

from tortoise import fields
from tortoise.backends.base.client import BaseDBAsyncClient
from tortoise.models import Model

from app.models.base_model import BaseModel
from app.models.participant import Participant
from app.models.question import Question


class Answer(BaseModel, Model):
    participant: fields.ForeignKeyRelation[Participant] = fields.ForeignKeyField(
        "models.Participant", related_name="answers", db_constraint=True
    )
    question: fields.ForeignKeyRelation[Question] = fields.ForeignKeyField(
        "models.Question", related_name="answers", db_constraint=True
    )
    choice = fields.CharField(max_length=5)

    class Meta:
        table = "answers"

    @classmethod
    async def get_all_answers(cls) -> list[Answer]:
        return await cls.all()

    @classmethod
    async def save_answer(
        cls, conn: BaseDBAsyncClient, participant_id: str, question_id: int | None, choice: str | None
    ) -> None:
        new_answer = Answer(participant_id=participant_id, question_id=question_id, choice=choice)
        await new_answer.save()

    @classmethod
    async def get_answers_join_questions(cls) -> list[Answer]:
        return await cls.filter().select_related("question").all()
