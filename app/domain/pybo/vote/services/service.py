from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.question.repositories.repository import QuestionRepository
from app.domain.pybo.user.repositories.repository import UserRepository
from app.domain.pybo.user.schemas.request import UserQueryRequest
from app.domain.pybo.user.schemas.response import UserItemResponse
from app.domain.pybo.vote.repositories.repository import VoteRepository


class VoteService():
    def __init__(self):
        self.question_repository = QuestionRepository()
        self.user_repository = UserRepository()
        self.vote_repository = VoteRepository()
    
    
    async def vote_question(self, db: AsyncSession, question_id: int, user: UserItemResponse):
        async with db.begin():
            question = await self.question_repository.find_question(db=db, question_id=question_id)
            user = await self.user_repository.find_user(db, {"username": user.username})

            await self.vote_repository.vote_question(user, question)