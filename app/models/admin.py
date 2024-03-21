from tortoise import fields
from tortoise.models import Model

from app.models.base_model import BaseModel


class Admin(BaseModel, Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=10)
    password = fields.CharField(max_length=50)
