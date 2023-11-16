from pydantic import BaseModel, validator
from typing import Literal
from datetime import datetime

# 사용자로부터 받아오는 값 처리하는 곳
class UserCreate(BaseModel):
    account: str
    password1: str
    password2: str
    name: str
    location: str
    user_type: Literal["0", "1"]
    # createdAt: datetime

    # 받아온 값 검증 
    @validator("account", "name", "password1", "password2", "location")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v

    @validator("password2")
    def passwords_match(cls, v, values):
        if "password1" in values and v != values["password1"]:
            raise ValueError("비밀번호가 일치하지 않습니다")
        return v

class Logout(BaseModel):
    pass


class Login(BaseModel):
    account: str
    password: str


class UserDelete(BaseModel):
    account: str
    password: str

class PostCreate(BaseModel):
    title: str
    content: str
    career: str
    edu: str
    start_date: datetime
    end_date: datetime
    is_public: str
    use_template: str
