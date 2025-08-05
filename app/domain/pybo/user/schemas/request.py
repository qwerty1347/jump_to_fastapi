from http import HTTPStatus
from fastapi import HTTPException
from pydantic import model_validator

from app.domain.pybo.user.schemas.base import UserBase


class UserCreateRequest(UserBase):
    username: str
    password1: str
    password2: str
    email: str

    @model_validator(mode="after")
    def validate_password(self):
        """
        비밀번호를 검증하는 메서드

        이 메서드는 password1과 password2가 동일한지 검증합니다.
        만약 서로 다르다면 HTTPException을 발생시킵니다.

        반환값:
        - self: 검증이 성공하면 현재 객체를 반환합니다.
        """
        if self.password1 != self.password2:
            raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="password1 and password2 must be same")

        return self


class UserCreateModel(UserBase):
    username: str
    password: str
    email: str


class UserQueryRequest(UserBase):
    username: str