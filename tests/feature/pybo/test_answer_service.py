import pytest

from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.answer.schemas.request import AnswerCreateRequest, AnswerUpdateRequest
from app.domain.pybo.answer.schemas.response import AnswerItemResponse
from app.domain.pybo.answer.services.service import AnswerService
from app.domain.pybo.user.schemas.response import UserItemResponse


@pytest.mark.asyncio
class TestAnswerService:
    async def async_setup(self):
        self.service = AnswerService()
        self.user = UserItemResponse(
            id=1,
            username="username",
            email="email",
            created_at="2025-08-14 00:00:00",
        )
   

    async def test_get_answer_by_question_id(self, db: AsyncSession):
        await self.async_setup()
        answers = await self.service.get_answers_by_question_id(db, 1)
        
        assert isinstance(answers, list)
        
        
    async def test_create_answer(self, db: AsyncSession):
        await self.async_setup()
        create_dto = AnswerCreateRequest(
            content="answer content",
            question_id=1
        )
        answer = await self.service.create_answer(db, create_dto, self.user)

        assert isinstance(answer, AnswerItemResponse)
        
        
    async def test_update_answer(self, db: AsyncSession):
        await self.async_setup()
        answer_id = 1
        update_dto = AnswerUpdateRequest(
            content="answer content"   
        )
        result = await self.service.update_answer(db, answer_id, update_dto, self.user)
        
        assert isinstance(result.rowcount, int)
        