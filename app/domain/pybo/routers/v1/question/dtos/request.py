from app.domain.pybo.routers.v1.question.dtos.base import QuestionBase


class QuestionRequest(QuestionBase):
    subject: str
    content: str