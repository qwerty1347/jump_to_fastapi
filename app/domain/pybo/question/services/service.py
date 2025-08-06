from http import HTTPStatus
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.question.schemas.request import QuestionCreateRequest, QuestionUpdateRequest, QuestionQueryRequest
from app.domain.pybo.question.schemas.response import QuestionItemResponse
from app.domain.pybo.question.repositories.repository import QuestionRepository
from common.response import error_response, success_response


class QuestionService():
    def __init__(self):
        self.question_repository = QuestionRepository()


    async def get_questions(self, db: AsyncSession, query_dto: QuestionQueryRequest) -> JSONResponse:
        """
        Question 리스트를 가져오는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - query_dto (QuestionQueryRequest): Question 리스트를 가져올 때의
            옵션을 정의하는 데이터를 전달합니다.

        반환값:
        - JSONResponse: Question 리스트가 포함된 성공 응답을 반환합니다.
        """
        try:
            skip = (query_dto.page - 1) * query_dto.size
            limit = query_dto.size

            response = await self.question_repository.get_questions(db, skip, limit)
            response_model = [QuestionItemResponse.model_validate(item) for item in response]

            return success_response(jsonable_encoder(response_model))

        except ValidationError as ve:
            raise RequestValidationError(errors=ve.errors())

        except Exception as e:
            return error_response(message=str(e))


    async def find_question(self, db: AsyncSession, question_id: int) -> JSONResponse:
        """
        Question 하나를 가져오는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - question_id (int): Question 하나의 고유 ID를 전달합니다.

        반환값:
        - JSONResponse: Question 하나가 포함된 성공 응답을 반환합니다.
        """
        try:
            response = await self.question_repository.find_question(db, question_id)

            if response is None:
                raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Question not found"
                                    )
            response_model = QuestionItemResponse.model_validate(response)

            return success_response(jsonable_encoder(response_model))

        except HTTPException as e:
            raise e

        except Exception as e:
            return error_response(message=str(e))


    async def create_question(self, db: AsyncSession, create_dto: QuestionCreateRequest) -> JSONResponse:
        """
        Question을 생성하는 비동기 서비스 (폼 데이터)

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - create_dto (QuestionCreateRequest): Question 생성을 위한 폼 데이터를 전달합니다.

        반환값:
        - JSONResponse: 생성된 Question 하나가 포함된 성공 응답을 반환합니다.
        """
        try:
            async with db.begin():
                response = await self.question_repository.create_question(db, create_dto.model_dump())
                
            response_model = QuestionItemResponse.model_validate(response)

            return success_response(jsonable_encoder(response_model), code=HTTPStatus.CREATED)

        except Exception as e:
            return error_response(message=str(e))


    async def update_question_by_question_id(self, db: AsyncSession, question_id: int, update_dto: QuestionUpdateRequest) -> JSONResponse:
        """
        Question을 수정하는 비동기 서비스 (폼 데이터)

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - question_id (int): Question 하나의 고유 ID를 전달합니다.
        - update_dto (QuestionUpdateRequest): Question 수정을 위한 폼 데이터를 전달합니다.

        반환값:
        - JSONResponse: 수정된 Question 하나가 포함된 성공 응답을 반환합니다.
        """
        try:
            async with db.begin():
                response = await self.question_repository.update_question_by_question_id(db, question_id, update_dto.model_dump(exclude_unset=True))

            return success_response({"rowcount": response})

        except Exception as e:
            return error_response(message=str(e))


    async def delete_question_by_question_id(self, db: AsyncSession, question_id: int) -> JSONResponse:
        """
        Question을 삭제하는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - question_id (int): Question 하나의 고유 ID를 전달합니다.

        반환값:
        - JSONResponse: 삭제된 Question의 개수가 포함된 성공 응답을 반환합니다.
        """
        try:
            async with db.begin():
                response = await self.question_repository.delete_question_by_question_id(db, question_id)
                
            return success_response({"rowcount": response})

        except Exception as e:
            error_response(message=str(e))