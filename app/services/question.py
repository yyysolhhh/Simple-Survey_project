from tortoise.backends.base.client import BaseDBAsyncClient

from app.models.question import Question


# async def get_questions(conn: BaseDBAsyncClient) -> int:
async def get_questions():
    # sql = "INSERT INTO participants(name, age, gender) VALUES (%s, %s, %s)"
    # participant_id: int = await conn.execute_insert(sql, [data.name, data.age, data.gender])
    questions = await Question.get_all_questions()
    questions_list = [question.content for question in questions]
    return questions_list
