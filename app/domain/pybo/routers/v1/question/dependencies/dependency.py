from fastapi import Body, Form, Query

from app.domain.pybo.routers.v1.question.dtos.request import QuestionRequest, QuestionUpdateRequest, QuestionQueryRequest


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


def parse_question_update_json_payload(update_dto: QuestionUpdateRequest = Body(...)) -> QuestionUpdateRequest:
    """
    Question을 수정하는 엔드포인트에서 사용하는 JSON 데이터를 반환하는 함수

    매개변수:
    - update_dto (QuestionUpdateRequest): Question 수정을 위한 JSON 데이터를 전달합니다.

    반환값:
    - QuestionUpdateRequest: Question 수정을 위한 JSON 데이터를 전달합니다.
    """
    return update_dto


def parse_questions_query(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=30)
) -> QuestionQueryRequest:
    """
    Question 리스트를 쿼리하는 엔드포인트에서 사용하는 쿼리 파라미터를 반환하는 함수

    매개변수:
    - page (int): 페이지 번호를 전달합니다. 기본값은 0입니다.
    - size (int): 페이지 당 Question의 개수를 전달합니다. 기본값은 10이며, 최소값은 1, 최대값은 30입니다.

    반환값:
    - QuestionQueryRequest: Question 리스트를 쿼리하기 위한 데이터를 전달합니다.
    """
    return QuestionQueryRequest(page=page, size=size)