from app.domain.pybo.answer.schemas.base import AnswerBase


class AnswerCreateRequest(AnswerBase):
    content: str
    question_id: int


class AnswerUpdateRequest(AnswerBase):
    content: str

    model_config = {
        "extra": "forbid"
    }


class AnswerQueryRequest(AnswerBase):
    page: int
    size: int