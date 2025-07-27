from http import HTTPStatus
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.answer.schemas.request import AnswerQueryRequest, AnswerCreateRequest, AnswerUpdateRequest
from app.domain.pybo.answer.schemas.response import AnswerItemResponse
from app.domain.pybo.answer.repositories.repository import AnswerRepository
from common.response import error_response, success_response


class AnswerService:
    def __init__(self):
        self.answer_repository = AnswerRepository()


    async def get_answers_by_question_id(self, db: AsyncSession, question_id: int) -> JSONResponse:
        """
        특정 질문 ID에 해당하는 answer 목록을 가져오는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - question_id (int): 특정 질문의 고유 ID를 전달합니다.

        반환값:
        - JSONResponse: 특정 질문에 해당하는 answer 목록이 포함된 성공 응답을 반환합니다.
        """
        response = await self.answer_repository.get_answers_by_question_id(db, question_id)
        response_model = [AnswerItemResponse.model_validate(item) for item in response]

        return success_response(jsonable_encoder(response_model))


    async def get_answers(self, db: AsyncSession, query_dto: AnswerQueryRequest) -> JSONResponse:
        """
        answer 목록을 가져오는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - query_dto (AnswerQueryRequest): answer 목록을 가져올 때의
            옵션을 정의하는 데이터를 전달합니다.

        반환값:
        - JSONResponse: answer 목록이 포함된 성공 응답을 반환합니다.
        """
        skip = (query_dto.page - 1) * query_dto.size
        limit = query_dto.size

        response = await self.answer_repository.get_answers(db, skip, limit)
        response_model = [AnswerItemResponse.model_validate(item) for item in response]

        return success_response(jsonable_encoder(response_model))


    async def get_answer(self, db: AsyncSession, answer_id: int) -> JSONResponse:
        """
        answer 하나를 가져오는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - answer_id (int): answer 하나의 고유 ID를 전달합니다.

        반환값:
        - JSONResponse: answer 하나가 포함된 성공 응답을 반환합니다.
        """
        response = await self.answer_repository.get_answer(db, answer_id)
        response_model  = AnswerItemResponse.model_validate(response)

        return success_response(jsonable_encoder(response_model))


    async def create_answer(self, db: AsyncSession, create_dto: AnswerCreateRequest) -> JSONResponse:
        """
        answer 하나를 생성하는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - create_dto (AnswerCreateRequest): answer 생성을 위한 폼 데이터를 전달합니다.

        반환값:
        - JSONResponse: 생성된 answer 하나가 포함된 성공 응답을 반환합니다.
        """
        try:
            async with db.begin():
                response = await self.answer_repository.create_answer(db, create_dto.model_dump())
                response_model = AnswerItemResponse.model_validate(response)

                return success_response(jsonable_encoder(response_model), HTTPStatus.CREATED)

        except Exception as e:
            error_response(message=str(e))


    async def update_answer(self, db: AsyncSession, answer_id: int, update_dto: AnswerUpdateRequest) -> JSONResponse:
        """
        answer 하나를 수정하는 비동기 서비스 (폼 데이터)

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - answer_id (int): answer 하나의 고유 ID를 전달합니다.
        - update_dto (AnswerUpdateRequest): answer 수정을 위한 폼 데이터를 전달합니다.

        반환값:
        - JSONResponse: 수정된 answer의 개수가 포함된 성공 응답을 반환합니다.
        """
        try:
            async with db.begin():
                response = await self.answer_repository.update_answer(db, answer_id, update_dto.model_dump())
                return success_response(jsonable_encoder({"rowcount": response}))

        except Exception as e:
            error_response(message=str(e))


    async def delete_answer(self, db: AsyncSession, answer_id: int) -> JSONResponse:
        """
        answer 하나를 삭제하는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - answer_id (int): answer 하나의 고유 ID를 전달합니다.

        반환값:
        - JSONResponse: 삭제된 answer의 개수가 포함된 성공 응답을 반환합니다.
        """
        try:
            async with db.begin():
                response = await self.answer_repository.delete_answer(db, answer_id)
                return success_response({"rowcount": response})

        except Exception as e:
            return error_response(message=str(e))
