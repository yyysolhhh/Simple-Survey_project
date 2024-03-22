from pydantic import BaseModel


class ParticipantResponse(BaseModel):
    name: str
    age: int
    gender: str
