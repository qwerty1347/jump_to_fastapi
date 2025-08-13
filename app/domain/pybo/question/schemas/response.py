from datetime import datetime

from app.domain.pybo.question.schemas.base import QuestionBase, QuestionResponseBase
from app.domain.pybo.user.schemas.response import UserItemResponse


class QuestionItemResponse(QuestionBase):
    id: int
    subject: str
    content: str
    user_id: int
    voter: list[UserItemResponse] | None = None
    created_at: datetime
    updated_at: datetime | None = None


class QuestionResponse(QuestionResponseBase):
    data: list[QuestionItemResponse]


class QuestionItemAffectResponse(QuestionBase):
    rowcount: int


class QuestionAffectResponse(QuestionResponseBase):
    data: QuestionItemAffectResponse