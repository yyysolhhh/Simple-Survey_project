from app.models.answer import Answer
from app.models.question import Question


async def get_result_graphs():
    participants = await Question.get_all_questions()
    answers = await Answer.get_all_answers()
