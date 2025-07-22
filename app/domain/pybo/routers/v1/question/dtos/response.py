from datetime import datetime
from typing import List
from openai import BaseModel

from app.domain.pybo.routers.v1.question.dtos.base import QuestionBase


class QuestionItemResponse(QuestionBase):
    id: int
    subject: str
    content: str
    created_at: datetime
    updated_at: datetime | None = None


class QuestionResponse(BaseModel):
    result: bool
    code: int
    data: List[QuestionItemResponse]