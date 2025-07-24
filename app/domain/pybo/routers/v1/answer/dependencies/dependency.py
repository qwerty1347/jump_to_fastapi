from fastapi import Body, Form, Query

from app.domain.pybo.routers.v1.answer.dtos.request import AnswerQueryRequest, AnswerRequest, AnswerUpdateRequest


def parse_answer_create_form(
    content = Form(...),
    question_id = Form(...)
) -> AnswerRequest:
    """
    Answer을 생성하는 엔드포인트에서 사용하는 폼 데이터를 반환하는 함수

    매개변수:
    - content (Form): Answer의 내용을 전달합니다.
    - question_id (Form): Answer이 속하는 Question의 고유 ID를 전달합니다.

    반환값:
    - AnswerRequest: Answer 생성을 위한 폼 데이터를 전달합니다.
    """
    return AnswerRequest.model_validate({"content": content, "question_id": question_id})


def parse_answer_update_form_payload(
    content = Form(...)
) -> AnswerUpdateRequest:
    """
    Answer을 수정하는 엔드포인트에서 사용하는 폼 데이터를 반환하는 함수

    매개변수:
    - content (Form): Answer의 내용을 전달합니다.

    반환값:
    - AnswerUpdateRequest: Answer 수정을 위한 폼 데이터를 전달합니다.
    """
    return AnswerUpdateRequest.model_validate({"content": content})


def parse_answer_update_json_payload(update_dto: AnswerUpdateRequest = Body(...)) -> AnswerUpdateRequest:
    """
    Answer을 수정하는 엔드포인트에서 사용하는 JSON 데이터를 반환하는 함수

    매개변수:
    - update_dto (AnswerUpdateRequest): Answer 수정을 위한 JSON 데이터를 전달합니다.

    반환값:
    - AnswerUpdateRequest: Answer 수정을 위한 JSON 데이터를 전달합니다.
    """
    return update_dto


def parse_answer_query() -> AnswerQueryRequest:
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=30)

    return AnswerQueryRequest(page=page, size=size)