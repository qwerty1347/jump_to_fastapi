import pytest

from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.question.schemas.request import QuestionCreateRequest, QuestionUpdateRequest
from app.domain.pybo.question.schemas.response import QuestionItemResponse
from app.domain.pybo.question.services.service import QuestionService
from app.domain.pybo.user.schemas.response import UserItemResponse


@pytest.mark.asyncio
class TestQuestionService:
    async def async_setup(self):
        self.service = QuestionService()
        self.user = UserItemResponse(
            id=1,
            username="username",
            email="email",
            created_at="2025-08-14 00:00:00",
        )


    async def test_create_question(self, db: AsyncSession):
        await self.async_setup()
        create_dto = QuestionCreateRequest(
            subject="test question title",
            content="test question content"
        )
        result = await self.service.create_question(db, create_dto, self.user)

        assert isinstance(result, QuestionItemResponse)


    async def test_update_question_by_question_id(self, db: AsyncSession):
        await self.async_setup()
        question_id = 2
        update_dto = QuestionUpdateRequest(
            subject="test question title update",
            content="test question content update"
        )
        result = await self.service.update_question_by_question_id(db, question_id, update_dto, self.user)

        assert isinstance(result.rowcount, int)


    async def test_delete_question_by_question_id(self, db: AsyncSession):
        await self.async_setup()
        question_id = 2
        result = await self.service.delete_question_by_question_id(db, question_id, self.user)

        assert isinstance(result.rowcount, int)