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
        response = await self.answer_repository.get_answers_by_question_id(db, question_id)
        response_model = [AnswerItemResponse.model_validate(item) for item in response]

        return success_response(jsonable_encoder(response_model))
