from http import HTTPStatus
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.question.services.service import QuestionService
from app.domain.pybo.user.schemas.response import UserItemResponse
from app.domain.pybo.vote.repositories.repository import VoteRepository


class VoteService():
    def __init__(self):
        self.question_service = QuestionService()
        self.vote_repository = VoteRepository()
    
    
    async def vote_question(self, db: AsyncSession, question_id: int, user: UserItemResponse):
        return {"result": "success"}