from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.routers.v1.answer.dtos.response import AnswerItemResponse
from app.domain.pybo.routers.v1.answer.repositories.repository import AnswerRepository
from common.response import success_response


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


    async def get_answers(self, db: AsyncSession) -> JSONResponse:
        """
        answer 리스트를 가져오는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

        반환값:
        - JSONResponse: answer 리스트가 포함된 성공 응답을 반환합니다.
        """
        response = await self.answer_repository.get_answers(db)
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