from app.domain.pybo.login.schemas.base import LoginBase


class LoginRequest(LoginBase):
    username: str
    password: str