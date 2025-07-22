from fastapi import Form

from app.domain.pybo.routers.v1.answer.dtos.request import AnswerRequest


def parse_answer_create_form(
    content = Form(...),
    question_id = Form(...)
) -> AnswerRequest:
    return AnswerRequest.model_validate({"content": content, "question_id": question_id})