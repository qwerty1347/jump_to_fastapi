from http import HTTPStatus
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from app.domain.pybo.auth.services.service import AuthService
from app.domain.pybo.user.schemas.response import UserItemResponse
from common.response import error_response


auth_service = AuthService()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/pybo/user/login/json")



async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserItemResponse:
    """
    현재 사용자를 가져옵니다.

    token을 확인하여 User 정보를 가져옵니다.

    매개변수:
    - token (str): 토큰을 전달합니다.

    반환값:
    - UserItemResponse: User 정보를 가져옵니다.
    """
    return await auth_service.validate_access_token(token)