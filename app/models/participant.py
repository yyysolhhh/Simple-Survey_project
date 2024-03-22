from sqlalchemy import Integer, Column, String

from configs.database_settings import Base

from models.base_model import BaseModel


class Participant(Base, BaseModel):
    __tablename__ = "participants"

    name = Column(String(10))
    age = Column(Integer)
    gender = Column(String(10))



# from __future__ import annotations
#
# from tortoise import fields
# from tortoise.models import Model
#
# from models.base_model import BaseModel
#
#
# class Participant(BaseModel, Model):
#     name = fields.CharField(max_length=10)
#     age = fields.IntField()
#     gender = fields.CharField(max_length=10, default="other")
#
#     class Meta:
#         table = "participants"
#
#     @classmethod
#     async def get_one_by_id(cls, id: int) -> Participant:
#         return await cls.get(id=id)
