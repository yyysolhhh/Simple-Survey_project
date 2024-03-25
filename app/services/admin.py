from passlib.context import CryptContext

from app.models.admin import Admin

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def create_new_admin(new_admin, conn):
    username = new_admin.username
    hashed_password = pwd_context.hash(new_admin.password)
    await Admin.save_admin(username, hashed_password, conn)


