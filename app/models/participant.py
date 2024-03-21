from tortoise import fields
from tortoise.models import Model

from app.models.base_model import BaseModel


class Participant(BaseModel, Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=10)
    age = fields.IntField()
    gender = fields.CharField(max_length=10, default="other")
