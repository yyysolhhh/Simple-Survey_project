from typing import Any

from tortoise.backends.base.client import BaseDBAsyncClient

from app.models.answer import Answer


async def collect_answers(data: dict[str, list[dict[str, Any]]], participant_id: str, conn: BaseDBAsyncClient) -> None:
    answers = data.get("answers", [])
    for answer in answers:
        question_id = answer.get("question_id")
        choice = answer.get("choice")
        await Answer.save_answer(conn, participant_id, question_id, choice)
