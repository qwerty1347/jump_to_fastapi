from app.domain.pybo.routers.v1.answer.dtos.base import AnswerBase


class AnswerRequest(AnswerBase):
    content: str
    question_id: int