from datetime import datetime
from typing import List
from pydantic import BaseModel

from app.domain.pybo.user.schemas.base import UserBase


class UserItemResponse(UserBase):
    id: int
    username: str
    email: str
    created_at: datetime
    updated_at: datetime | None = None


class UserResponse(BaseModel):
    result: bool
    code: int
    data: List[UserItemResponse]