from fastapi import Form

from app.domain.pybo.user.schemas.request import UserCreateRequest


def parse_user_create_form_payload(
    username = Form(...),
    password1 = Form(...),
    password2 = Form(...),
    email = Form(...)
) -> UserCreateRequest:
    """
    User 생성을 위한 폼 데이터를 반환하는 함수

    매개변수:
    - username (Form): User의 username을 전달합니다.
    - password1 (Form): User의 비밀번호를 전달합니다.
    - password2 (Form): User의 비밀번호 확인을 전달합니다.
    - email (Form): User의 이메일을 전달합니다.

    반환값:
    - UserCreateRequest: User 생성을 위한 폼 데이터를 전달합니다.
    """
    return UserCreateRequest.model_validate({"username": username, "password1": password1, "password2": password2, "email": email})