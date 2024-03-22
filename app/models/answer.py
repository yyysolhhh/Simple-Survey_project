from tortoise import fields
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
