from app.domain.pybo.routers.v1.answer.dtos.base import AnswerBase


class AnswerRequest(AnswerBase):
    content: str
    question_id: int


class AnswerUpdateRequest(AnswerBase):
    content: str

    model_config = {
        "extra": "forbid"
    }


class AnswerQueryRequest:
    page: int
    size: int