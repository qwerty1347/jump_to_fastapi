from datetime import datetime
from typing import List

from openai import BaseModel

from app.domain.pybo.answer.dtos.base import AnswerBase


class AnswerItemResponse(AnswerBase):
    id: int
    content: str
    question_id: int
    created_at: datetime
    update_at: datetime | None = None


class AnswerResponse(BaseModel):
    result: bool
    code: int
    data: List[AnswerItemResponse]