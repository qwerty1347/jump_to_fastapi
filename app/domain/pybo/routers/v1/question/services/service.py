from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.routers.v1.question.repositories.repository import QuestionRepository
from common.response import error_response


class QuestionService():
    def __init__(self):
        self.question_repository = QuestionRepository()

    async def get_question_list(self, db: AsyncSession):
        try:
            return await self.question_repository.get_question_list(db)

        except Exception as e:
            return error_response(message=str(e))