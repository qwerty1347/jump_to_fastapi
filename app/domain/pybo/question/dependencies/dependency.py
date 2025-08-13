from fastapi import Body, Form, Query

from app.domain.pybo.question.schemas.request import QuestionCreateRequest, QuestionUpdateRequest, QuestionQueryRequest


def parse_question_create_form(
    subject = Form(...),
    content = Form(...)
) -> QuestionCreateRequest:
    """
    Question을 생성하는 엔드포인트에서 사용하는 폼 데이터를 반환하는 함수

    매개변수:
    - subject (Form): Question 제목을 전달합니다.
    - content (Form): Question 내용을 전달합니다.

    반환값:
    - QuestionCreateRequest: Question 생성을 위한 폼 데이터를 전달합니다.
    """
    return QuestionCreateRequest.model_validate({"subject": subject, "content": content})


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
    size: int = Query(10, ge=1, le=30),
    sc: str | None = Query(None),
    query: str | None = Query(None)
) -> QuestionQueryRequest:
    """
    Question 리스트를 가져오는 쿼리 파라미터를 파싱하는 함수

    매개변수:
    - page (int): 페이지 번호를 전달합니다. 기본값은 1이며, 1 이상의 값을 가집니다.
    - size (int): 페이지당 Question의 개수를 전달합니다. 기본값은 10이며, 1 이상 30 이하의 값을 가집니다.
    - sc (str | None): 검색 카테고리를 전달합니다. 기본값은 None입니다.
    - query (str | None): 검색어를 전달합니다. 기본값은 None입니다.

    반환값:
    - QuestionQueryRequest: Question 리스트를 가져오기 위한 쿼리 데이터를 전달합니다.
    """
    return QuestionQueryRequest(page=page, size=size, sc=sc, query=query)