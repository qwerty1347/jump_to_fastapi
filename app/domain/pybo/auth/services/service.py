from datetime import datetime, timedelta, timezone
from http import HTTPStatus
from fastapi import HTTPException
from jose import jwt

from app.domain.pybo.user.schemas.response import UserItemResponse
from app.domain.pybo.user.schemas.request import UserQueryRequest
from app.domain.pybo.user.services.service import UserService
from config.settings import settings
from databases.mysql.session import async_session


class AuthService():
    def __init__(self):
        self.user_service = UserService()


    def create_access_token(self, username: str) -> dict[str, str]:
        """사용자 인증 정보를 확인하여 access_token을 생성하는 동기 메서드

        매개변수:
        - username (str): 사용자의 username을 전달합니다.

        반환값:
        - dict[str, str]: 생성된 access_token이 포함된 성공 응답을 반환합니다.
        """
        data = {
            "sub": username,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=settings.PYBO_JWT_EXPIRE_MINUTES)
        }

        return {
            "access_token": jwt.encode(data, settings.PYBO_JWT_SECRET_KEY, algorithm=settings.PYBO_JWT_ALGORITHM),
            "token_type": "bearer",
            "username": username
        }


    async def validate_access_token(self, token: str) -> str:
        """토큰을 확인하여 사용자 정보를 가져오는 비동기 메서드

        매개변수:
        - token (str): 토큰을 전달합니다.

        반환값:
        - username (str): 토큰에 포함된 username을 가져옵니다.
        """
        payload = jwt.decode(token, settings.PYBO_JWT_SECRET_KEY, algorithms=[settings.PYBO_JWT_ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Invalid token")

        return username


    async def find_authenticated_user(self, username: str) -> UserItemResponse:
        """토큰을 확인하여 사용자 정보를 가져오는 비동기 메서드

        매개변수:
        - username (str): 토큰에 포함된 username을 전달합니다.

        반환값:
        - UserItemResponse: User 정보를 가져옵니다.
        """
        async with async_session() as db:
            return await self.user_service.find_user(db=db, query_dto=UserQueryRequest(username=username))