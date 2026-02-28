from pydantic import BaseModel


class UserRegister(BaseModel):
    first_name: str
    last_name: str
    age: int


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class QParams(BaseModel):
    pageram: str | None = None
    eewewe: str = "login"

    class Config:
        from_attributes = True
