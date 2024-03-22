from sqlalchemy import Column, String

from configs.database_settings import Base

from models.base_model import BaseModel


class Admin(Base, BaseModel):
    __tablename__ = 'admins'

    username = Column(String(10))
    password = Column(String(50))


# from tortoise import fields
# from tortoise.models import Model
#
# from app.models.base_model import BaseModel
# class Admin(BaseModel, Model):
#     username = fields.CharField(max_length=10)
#     password = fields.CharField(max_length=50)
#
#     class Meta:
#         table = "admins"
