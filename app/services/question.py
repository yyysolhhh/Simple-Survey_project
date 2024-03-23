from typing import Any

from fastapi.encoders import jsonable_encoder

from app.models.question import Question


async def get_questions() -> list[str]:
    questions: list[Question] = await Question.get_all_questions()
    questions_list: list[str] = [question.content for question in questions]
    return questions_list


async def get_active_questions() -> list[str]:
    questions: list[Question] = await Question.get_all_active_questions()
    questions_list: list[dict[str, Any]] = [
        {
            "id": question.id,
            "content": question.content,
            "order_num": question.order
        }
        for question in questions
    ]
    return jsonable_encoder(questions_list)
