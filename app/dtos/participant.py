from pydantic import BaseModel


class ParticipantRequest(BaseModel):
    name: str
    age: int
    gender: str


class ParticipantResponse(BaseModel):
    name: str
    age: int
    gender: str
