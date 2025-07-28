from fastapi import Form

from app.domain.pybo.user.schemas.request import UserCreateRequest


def parse_user_create_form_payload(
    username = Form(...),
    password1 = Form(...),
    password2 = Form(...),
    email = Form(...)
) -> UserCreateRequest:
    return UserCreateRequest.model_validate({"username": username, "password1": password1, "password2": password2, "email": email})