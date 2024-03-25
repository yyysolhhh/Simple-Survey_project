from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class Admin(BaseModel):
    username: str

class AdminInDB(Admin):
    hashed_password: str


