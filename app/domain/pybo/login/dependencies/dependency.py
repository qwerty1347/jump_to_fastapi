from fastapi import Form

from app.domain.pybo.login.schemas.request import LoginRequest


def parse_login_form(
    username: str = Form(...),
    password: str = Form(...)
) -> LoginRequest:
    """
    로그인 폼 데이터를 반환하는 함수

    매개변수:
    - username (Form): User의 username을 전달합니다.
    - password (Form): User의 비밀번호를 전달합니다.

    반환값:
    - LoginRequest: 로그인 폼 데이터를 전달합니다.
    """
    return LoginRequest.model_validate({"username": username, "password": password})