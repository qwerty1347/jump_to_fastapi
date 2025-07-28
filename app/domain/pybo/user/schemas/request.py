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
        if self.password1 != self.password2:
            raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="password1 and password2 must be same")

        return self