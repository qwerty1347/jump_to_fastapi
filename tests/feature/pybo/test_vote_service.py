import pytest

from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.user.schemas.response import UserItemResponse
from app.domain.pybo.vote.services.service import VoteService


@pytest.mark.asyncio
class TestVoteService:
    async def async_setup(self):
        self.service = VoteService()
        self.user = UserItemResponse(
            id=1,
            username="test1",
            email="test1@gmail.com",
            created_at="2025-08-14 00:00:00",
        )


    async def test_vote_question(self, db: AsyncSession):
        await self.async_setup()
        question_id = 1
        result = await self.service.vote_question(db, question_id, self.user)

        assert result is None


    async def test_vote_answer(self, db: AsyncSession):
        await self.async_setup()
        answer_id = 1
        result = await self.service.vote_answer(db, answer_id, self.user)

        assert result is None