from http import HTTPStatus
from fastapi import HTTPException
from pydantic import model_validator
from app.domain.pybo.routers.v1.question.dtos.base import QuestionBase


class QuestionRequest(QuestionBase):
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