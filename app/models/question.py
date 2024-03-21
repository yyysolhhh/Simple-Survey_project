from tortoise import fields
from tortoise.models import Model

from app.models.base_model import BaseModel


class Question(BaseModel, Model):
    id = fields.BigIntField(pk=True)
    order = fields.IntField()
    is_active = fields.BooleanField(default=True)
    content = fields.TextField()
