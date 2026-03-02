from pydantic import BaseModel
from typing import str

class AddressCreate(BaseModel):
    full_name: str
    phone: str
    country: str
    city: str
    street: str
    is_default: bool = False


class AddressUpdate(BaseModel):
    full_name: str | None = None
    phone: str | None = None
    country: str | None = None
    city: str | None = None
    street: str | None = None
    is_default: bool | None = None


class AddressResponse(BaseModel):
    id: int
    full_name: str
    phone: str
    country: str
    city: str
    street: str
    is_default: bool

    model_config = {"from_attributes": True}
