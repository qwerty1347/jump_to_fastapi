from datetime import datetime

from app.domain.pybo.answer.schemas.base import AnswerAffectResponse, AnswerBase
from app.domain.pybo.user.schemas.response import UserItemResponse


class AnswerItemResponse(AnswerBase):
    id: int
    content: str
    question_id: int
    user_id: int
    voter: list[UserItemResponse] | None = None
    created_at: datetime
    update_at: datetime | None = None


class AnswerResponse(AnswerAffectResponse):
    data: list[AnswerItemResponse]


class AnswerItemAffectedResponse(AnswerBase):
    rowcount: int


class AnswerAffectedResponse(AnswerAffectResponse):
    data: AnswerItemAffectedResponse