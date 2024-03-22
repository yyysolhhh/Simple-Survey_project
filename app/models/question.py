from tortoise import fields
from tortoise.models import Model

from app.models.base_model import BaseModel


class Question(BaseModel, Model):
    order = fields.IntField()
    is_active = fields.BooleanField(default=True)
    content = fields.TextField()

    class Meta:
        table = "questions"

    @classmethod
    async def get_all_questions(cls):
        return await cls.all()
