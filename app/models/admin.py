from __future__ import annotations

from tortoise import fields
from tortoise.backends.base.client import BaseDBAsyncClient
from tortoise.models import Model
from tortoise.queryset import QuerySetSingle

from app.dtos.admin import AdminInDB
from app.models.base_model import BaseModel


class Admin(BaseModel, Model):
    username = fields.CharField(max_length=10, unique=True)
    password = fields.CharField(max_length=100)

    class Meta:
        table = "admins"

    @classmethod
    def get_admin(cls, username: str) -> QuerySetSingle[Admin | None]:
        return cls.filter(username=username).first()

    @classmethod
    async def save_admin(cls, username: str, password: str, conn: BaseDBAsyncClient) -> None:
        await cls.create(username=username, password=password)
