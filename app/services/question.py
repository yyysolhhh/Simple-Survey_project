from tortoise.backends.base.client import BaseDBAsyncClient

from app.models.question import Question


# async def get_questions(conn: BaseDBAsyncClient) -> int:
async def get_questions() -> list[str]:
    questions: list[Question] = await Question.get_all_questions()
    questions_list: list[str] = [question.content for question in questions]
    return questions_list
