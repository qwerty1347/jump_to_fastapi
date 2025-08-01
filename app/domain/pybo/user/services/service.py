from http import HTTPStatus
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.domain.pybo.user.repositories.repository import UserRepository
from app.domain.pybo.user.schemas.request import UserCreateModel
from app.domain.pybo.user.schemas.response import UserItemResponse
from common.response import error_response, success_response
from common.utils.hash import hash_context


class UserService():
    def __init__(self):
        self.user_repository = UserRepository()


    async def create_user(self, db, create_dto) -> JSONResponse:
        """
        User을 생성하는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - create_dto (UserCreateModel): User 생성을 위한 폼 데이터를 전달합니다.

        반환값:
        - JSONResponse: 생성된 User 하나가 포함된 성공 응답을 반환합니다.
        """
        try:
            async with db.begin():
                is_user_exists = await self.user_repository.is_user_exists(db, create_dto.username, create_dto.email)

                if is_user_exists:
                    return error_response(code=HTTPStatus.CONFLICT, message="User already exists")

                create_dto = UserCreateModel(
                    username=create_dto.username,
                    password=hash_context(create_dto.password1),
                    email=create_dto.email
                )
                response = await self.user_repository.create_user(db, UserCreateModel.model_dump(create_dto))
                response_model = UserItemResponse.model_validate(response)

                return success_response(jsonable_encoder(response_model), HTTPStatus.CREATED)

        except Exception as e:
            return error_response(message=str(e))
