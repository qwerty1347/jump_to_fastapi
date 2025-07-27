from app.domain.pybo.question.schemas.base import QuestionBase


class QuestionCreateRequest(QuestionBase):
    subject: str
    content: str


class QuestionUpdateRequest(QuestionBase):
    subject: str | None = None
    content: str | None = None

    model_config = {
        "extra": "forbid"
    }


class QuestionQueryRequest(QuestionBase):
    page: int
    size: int
    keyword: str | None = None