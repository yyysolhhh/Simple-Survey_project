from passlib.context import CryptContext
from tortoise.backends.base.client import BaseDBAsyncClient

from app.dtos.admin import AdminInDB
from app.models.admin import Admin

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def create_new_admin(new_admin: AdminInDB, conn: BaseDBAsyncClient) -> None:
    username = new_admin.username
    hashed_password = pwd_context.hash(new_admin.password)
    await Admin.save_admin(username, hashed_password, conn)
