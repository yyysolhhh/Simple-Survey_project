from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from app.configs import settings

# 동기용 데이터 베이스 설정
SQLALCHEMY_DATABASE_URL = \
    f"mysql+pymysql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DB_DB}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# 비동기용 데이터 베이스 설정 -> aiomysql

ASYNC_SQLALCHEMY_DATABASE_URL = \
    f'mysql+aiomysql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DB_DB}'
async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession)

Base = declarative_base()


# from app.configs import settings
#
# TORTOISE_APP_MODELS = [
#     "app.models.admin",
#     "app.models.participant",
#     "app.models.answer",
#     "app.models.question",
#     "aerich.models",
# ]
#
# TORTOISE_ORM = {
#     "connections": {
#         "default": {
#             "engine": "tortoise.backends.mysql",
#             "credentials": {
#                 "host": settings.DB_HOST,
#                 "port": settings.DB_PORT,
#                 "user": settings.DB_USER,
#                 "password": settings.DB_PASSWORD,
#                 "database": settings.DB_DB,
#                 "connect_timeout": 5,
#             },
#         },
#     },
#     "apps": {
#         "models": {
#             "models": TORTOISE_APP_MODELS,
#         },
#     },
#     # "routers": ["app.configs.database_config.Router"],
#     "timezone": "Asia/Seoul",
# }
