from datetime import datetime
from pydantic import BaseModel

from app.domain.pybo.user.schemas.base import UserBase


class UserItemResponse(UserBase):
    id: int
    username: str
    email: str
    created_at: datetime
    updated_at: datetime | None = None


class UserLoginResponse(UserBase):
    password: str


class UserResponse(BaseModel):
    result: bool
    code: int
    data: list[UserItemResponse]