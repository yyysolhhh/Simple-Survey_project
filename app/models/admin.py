from tortoise import fields
from tortoise.models import Model
from tortoise.backends.base.client import BaseDBAsyncClient

from app.dtos.admin import AdminInDB
from app.models.base_model import BaseModel


class Admin(BaseModel, Model):
    username = fields.CharField(max_length=10, unique=True)
    password = fields.CharField(max_length=100)

    class Meta:
        table = "admins"

    @classmethod
    def get_admin(cls, username: str):
        return cls.get_or_none(username=username)

    @classmethod
    def save_admin(cls, username, password, conn: BaseDBAsyncClient):
        return cls.create(username=username, password=password)
