from models.participant import Participant


async def get_participant(name: str, age: int, gender: str) -> None:
    participant = Participant(name=name, age=age, gender=gender)
    # print(participant.name)
    await participant.save()
    # participant = await Participant.create(name=name, age=age, gender=gender)
    # participant = await Participant.get_one_by_id(id=1)
    # print(participant)
    # await Participant.create(name=name, age=age, gender=gender)

    # print("pt", participant)
    # return participant.get_one_by_id(1)
    # return participant
