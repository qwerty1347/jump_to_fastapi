from datetime import datetime
from typing import List
from pydantic import BaseModel

from app.domain.pybo.question.schemas.base import QuestionBase


class QuestionItemResponse(QuestionBase):
    id: int
    subject: str
    content: str
    user_id: int
    created_at: datetime
    updated_at: datetime | None = None


class QuestionResponse(BaseModel):
    result: bool
    code: int
    data: List[QuestionItemResponse]