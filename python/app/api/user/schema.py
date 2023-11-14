from pydantic import BaseModel, validator
from typing import Literal

class UserCreate(BaseModel):
    user_id: str
    password1: str
    password2: str
    name: str
    location: str

    @validator("user_id", "name", "password1", "password2", "location")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v

    @validator("password2")
    def passwords_match(cls, v, values):
        if "password1" in values and v != values["password1"]:
            raise ValueError("비밀번호가 일치하지 않습니다")
        return v