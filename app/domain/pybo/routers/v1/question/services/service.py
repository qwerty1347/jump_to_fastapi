from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.routers.v1.question.dtos.response import QuestionResponse
from app.domain.pybo.routers.v1.question.repositories.repository import QuestionRepository
from common.response import error_response, success_response


class QuestionService():
    def __init__(self):
        self.question_repository = QuestionRepository()

    async def get_question_list(self, db: AsyncSession):
        try:
            response = await self.question_repository.get_question_list(db)
            response_model = [QuestionResponse.model_validate(item) for item in response]

            return success_response(jsonable_encoder(response_model))

        except ValidationError as ve:
            raise RequestValidationError(errors=ve.errors())

        except Exception as e:
            return error_response(message=str(e))