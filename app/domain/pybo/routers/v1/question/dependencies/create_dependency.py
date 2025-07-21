from fastapi import Form

from app.domain.pybo.routers.v1.question.dtos.request import QuestionRequest


def get_question_form_data(
    subject = Form(...),
    content = Form(...)
) -> QuestionRequest:
    return QuestionRequest.model_validate({"subject": subject, "content": content})