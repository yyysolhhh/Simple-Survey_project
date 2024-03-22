from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, DateTime


class BaseModel:
    id = Column(BigInteger, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    modified_at = Column(DateTime, onupdate=datetime.utcnow)



# from tortoise import fields
#
#
# class BaseModel:
#     id = fields.BigIntField(pk=True)
#     created_at = fields.DatetimeField(auto_now_add=True)
#     modified_at = fields.DatetimeField(auto_now=True)
