from tortoise import fields
from tortoise.models import Model

from app.models.base_model import BaseModel


class Answer(BaseModel, Model):
    id = fields.BigIntField(pk=True)
    participant_id = fields.ForeignKeyField(
        "models.Participant",
        related_name="answers",
        db_constraint=False
    )
    question_id = fields.ForeignKeyField(
        "models.Question",
        related_name="answers",
        db_constraint=False
    )
    choice = fields.BooleanField()
    