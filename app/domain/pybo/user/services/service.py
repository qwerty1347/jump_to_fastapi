from http import HTTPStatus
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.user.repositories.repository import UserRepository
from app.domain.pybo.user.schemas.request import UserCreateModel, UserCreateRequest, UserQueryRequest
from app.domain.pybo.user.schemas.response import UserItemResponse
from common.utils.hash import hash_context


class UserService():
    def __init__(self):
        self.user_repository = UserRepository()


    async def create_user(self, db: AsyncSession, create_dto: UserCreateRequest) -> UserItemResponse:
        """
        User을 생성하는 비동기 메서드

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - create_dto (UserCreateRequest): User 생성을 위한 폼 데이터를 전달합니다.

        반환값:
        - UserItemResponse: 생성된 User 하나가 포함된 성공 응답을 반환합니다.
        """
        async with db.begin():
            is_user_exists = await self.user_repository.is_user_exists(db, create_dto.username, create_dto.email)

            if is_user_exists:
                raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="User already exists")

            create_dto = UserCreateModel(
                username=create_dto.username,
                password=hash_context(create_dto.password1),
                email=create_dto.email
            )
            response = await self.user_repository.create_user(db, UserCreateModel.model_dump(create_dto))

        return UserItemResponse.model_validate(response)


    async def find_user(self, db: AsyncSession, query_dto: UserQueryRequest) -> UserItemResponse:
        """
        User 하나를 가져오는 비동기 메서드

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - query_dto (UserQueryRequest): User 가져올 때 사용할 조건을 전달합니다.

        반환값:
        - UserItemResponse: User 하나가 포함된 성공 응답을 반환합니다.
        """
        async with db.begin():
            response = await self.user_repository.find_user(db, query_dto.model_dump(exclude_unset=True))

        if response is None:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="User not found")

        return UserItemResponse.model_validate(response)