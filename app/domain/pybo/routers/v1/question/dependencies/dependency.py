from fastapi import Body, Form

from app.domain.pybo.routers.v1.question.dtos.request import QuestionRequest, QuestionUpdateRequest


def parse_question_create_form(
    subject = Form(...),
    content = Form(...)
) -> QuestionRequest:
    """
    Question을 생성하는 엔드포인트에서 사용하는 폼 데이터를 반환하는 함수

    매개변수:
    - subject (Form): Question 제목을 전달합니다.
    - content (Form): Question 내용을 전달합니다.

    반환값:
    - QuestionRequest: Question 생성을 위한 폼 데이터를 전달합니다.
    """
    return QuestionRequest.model_validate({"subject": subject, "content": content})


def parse_question_update_form_payload(
    subject = Form(...),
    content = Form(...)
) -> QuestionUpdateRequest:
    """
    Question을 수정하는 엔드포인트에서 사용하는 폼 데이터를 반환하는 함수

    매개변수:
    - subject (Form): Question 제목을 전달합니다.
    - content (Form): Question 내용을 전달합니다.

    반환값:
    - QuestionUpdateRequest: Question 수정을 위한 폼 데이터를 전달합니다.
    """
    return QuestionUpdateRequest.model_validate({"subject": subject, "content": content})


def parse_question_update_json_payload(json_data: QuestionUpdateRequest = Body(...)) -> QuestionUpdateRequest:
    """
    Question을 수정하는 엔드포인트에서 사용하는 JSON 데이터를 반환하는 함수

    매개변수:
    - json_data (QuestionUpdateRequest): Question 수정을 위한 JSON 데이터를 전달합니다.

    반환값:
    - QuestionUpdateRequest: Question 수정을 위한 JSON 데이터를 전달합니다.
    """
    return json_data