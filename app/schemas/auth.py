from pydantic import BaseModel


class UserRegister(BaseModel):
    first_name: str
    last_name: str
    age: int


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


