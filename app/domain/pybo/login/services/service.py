from http import HTTPStatus
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.auth.services.service import AuthService
from app.domain.pybo.login.schemas.request import LoginRequest
from app.domain.pybo.user.repositories.repository import UserRepository
from app.domain.pybo.user.schemas.response import UserLoginResponse
from common.response import error_response, success_response
from common.utils.hash import verify_context


class LoginService():
    def __init__(self):
        self.auth_service = AuthService()
        self.user_repository = UserRepository()
    
        
    async def login_for_access_token(self, db: AsyncSession, login_dto: LoginRequest) -> dict[str, str]:
        """
        username과 password로 access_token을 생성하는 비동기 메서드
        
        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - login_dto (dict): User 인증을 위한 폼 데이터를 전달합니다.
        
        반환값:
        - dict[str, str]: 생성된 access_token이 포함된 성공 응답을 반환합니다.
        """
        return self.auth_service.create_access_token(login_dto.username)
            
    
    async def is_authenticated_user(self, db: AsyncSession, login_dto: LoginRequest):
        """
        username과 password로 User가 인증된 사용자인지 확인하는 비동기 메서드
        
        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - login_dto (dict): User 인증을 위한 폼 데이터를 전달합니다.
        
        반환값:
        - UserLoginResponse: User 인증이 성공하면 UserLoginResponse 하나가 포함된 성공 응답을 반환합니다.
        """
        response_model: UserLoginResponse = await self.find_user(db, login_dto.username)
        
        if not verify_context(login_dto.password, response_model.password):
            raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Invalid password")
        
    
    async def find_user(self, db: AsyncSession, username: str) -> UserLoginResponse:
        """
        User를 username으로 가져오는 비동기 메서드

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - username (str): User의 username을 전달합니다.

        반환값:
        - UserLoginResponse: User 하나가 포함된 성공 응답을 반환합니다.
        """
        async with db.begin():
            response = await self.user_repository.find_user(db, {"username": username})
            
        if response is None:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
        
        return UserLoginResponse.model_validate(response)
    