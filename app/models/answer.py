from sqlalchemy import Integer, Column, ForeignKey, String

from configs.database_settings import Base
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Answer(Base, BaseModel):
    __tablename__ = 'answers'

    participant_id = Column(Integer, ForeignKey('participant.id'))
    question_id = Column(Integer, ForeignKey('question.id'))
    choice = Column(String(100))

    participant = relationship('Participant', backref='answers')
    question = relationship('Question', backref='answers')
    # participant = relationship('Participant', back_populates='answers')
    # question = relationship('Question', back_populates='answers')


# from tortoise import fields
# from tortoise.models import Model
#
# from app.models.base_model import BaseModel
# from app.models.participant import Participant
# from app.models.question import Question
#
#
# class Answer(BaseModel, Model):
#     participant_id: fields.ForeignKeyRelation[Participant] = fields.ForeignKeyField(
#         "models.Participant", related_name="answers", db_constraint=False
#     )
#     question_id: fields.ForeignKeyRelation[Question] = fields.ForeignKeyField(
#         "models.Question", related_name="answers", db_constraint=False
#     )
#     choice = fields.BooleanField()
#
#     class Meta:
#         table = "answers"
