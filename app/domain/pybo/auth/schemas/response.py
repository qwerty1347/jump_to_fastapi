from app.domain.pybo.auth.schemas.base import AuthBase


class TokenItemResponse(AuthBase):
    access_token: str
    token_type: str
    username: str