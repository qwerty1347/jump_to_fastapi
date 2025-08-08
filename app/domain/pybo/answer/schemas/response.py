from datetime import datetime
from typing import List
from pydantic import BaseModel

from app.domain.pybo.answer.schemas.base import AnswerBase


class AnswerItemResponse(AnswerBase):
    id: int
    content: str
    question_id: int
    user_id: int
    created_at: datetime
    update_at: datetime | None = None


class AnswerResponse(BaseModel):
    result: bool
    code: int
    data: List[AnswerItemResponse]