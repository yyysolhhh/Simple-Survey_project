from app.models.answer import Answer
from app.models.question import Question


def get_result_graphs():
    participants = Question.get_all_questions()
    answers = Answer.get_all_answers()

