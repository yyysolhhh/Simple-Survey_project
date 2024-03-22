# from models.participant import Participant

# from dtos.participant import ParticipantResponse

from app.dtos.participant import ParticipantRequest
from tortoise import Tortoise

from app.configs.database_settings import TORTOISE_ORM


async def get_participant(data: ParticipantRequest):
    # participant = Participant(**data.dict())
    # print("1", participant)
    # await participant.save()

    await Tortoise.init(TORTOISE_ORM)

    conn = Tortoise.get_connection("default")
    # participant = data.dict()
    sql = "INSERT INTO participants(name, age, gender) VALUES (%s, %s, %s)"
    res = await conn.execute_insert(sql, (data.name, data.age, data.gender))
    return res


# async def get_participant(name: str, age: int, gender: str) -> None:
    # participant = Participant(name=name, age=age, gender=gender)
    # participant = Participant({"name": name, "age": age, "gender"= gender})
    # print(participant.name)
    # await participant.save()
    # participant = await Participant.create(name=name, age=age, gender=gender)
    # participant = await Participant.get_one_by_id(id=1)
    # print(participant)
    # await Participant.create(name=name, age=age, gender=gender)

    # print("pt", participant)
    # return participant.get_one_by_id(1)
    # return participant
