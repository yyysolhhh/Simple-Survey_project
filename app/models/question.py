from sqlalchemy import Integer, Column, ForeignKey, String, Boolean

from configs.database_settings import Base
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Question(Base, BaseModel):
    __tablename__ = 'questions'

    order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    content = Column(String(300))


# from tortoise import fields
# from tortoise.models import Model
#
# from app.models.base_model import BaseModel
#
#
# class Question(BaseModel, Model):
#     order = fields.IntField()
#     is_active = fields.BooleanField(default=True)
#     content = fields.TextField()
#
#     class Meta:
#         table = "questions"
