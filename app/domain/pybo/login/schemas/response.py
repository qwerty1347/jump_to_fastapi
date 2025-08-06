from pydantic import BaseModel

from app.domain.pybo.auth.schemas.response import TokenItemResponse


class LoginTokenResponse(BaseModel):
    result: bool
    code: int
    data: TokenItemResponse