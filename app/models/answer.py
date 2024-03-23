from tortoise import fields
from tortoise.backends.base.client import BaseDBAsyncClient
from tortoise.models import Model

from app.models.base_model import BaseModel
from app.models.participant import Participant
from app.models.question import Question


class Answer(BaseModel, Model):
    participant_id: fields.ForeignKeyRelation[Participant] = fields.ForeignKeyField(
        "models.Participant", related_name="answers", db_constraint=False
    )
    question_id: fields.ForeignKeyRelation[Question] = fields.ForeignKeyField(
        "models.Question", related_name="answers", db_constraint=False
    )
    choice = fields.BooleanField()

    class Meta:
        table = "answers"

    @classmethod
    async def save_answer(
        cls, conn: BaseDBAsyncClient, participant_id: str, question_id: int | None, choice: str | None
    ) -> None:
        # sql = "INSERT INTO answers (participant_id, question_id, choice)"
        new_answer = Answer(participant_id_id=participant_id, question_id_id=question_id, choice=choice)
        await new_answer.save()
