from http import HTTPStatus
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.answer.repositories.repository import AnswerRepository
from app.domain.pybo.question.repositories.repository import QuestionRepository
from app.domain.pybo.user.repositories.repository import UserRepository
from app.domain.pybo.user.schemas.response import UserItemResponse
from app.domain.pybo.vote.repositories.repository import VoteRepository


class VoteService():
    def __init__(self):
        self.question_repository = QuestionRepository()
        self.answer_repository = AnswerRepository()
        self.user_repository = UserRepository()
        self.vote_repository = VoteRepository()


    async def vote_question(self, db: AsyncSession, question_id: int, user: UserItemResponse):
        """
        질문 하나에 대한 추천을 처리하는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - question_id (int): Question 하나의 고유 ID를 전달합니다.
        - user (UserItemResponse): 사용자의 정보를 포함하는 UserItemResponse를 전달합니다.

        반환값:
        - None: None을 반환합니다.
        """
        async with db.begin():
            question = await self.question_repository.find_question(db=db, question_id=question_id)

            if question is None:
                raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Question not found")

            user = await self.user_repository.find_user(db, {"username": user.username})

            await self.vote_repository.vote_question(user, question)


    async def vote_answer(self, db: AsyncSession, answer_id: int, user: UserItemResponse):
        """
        답변 하나에 대한 추천을 처리하는 비동기 서비스

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - answer_id (int): answer 하나의 고유 ID를 전달합니다.
        - user (UserItemResponse): 사용자의 정보를 포함하는 UserItemResponse를 전달합니다.

        반환값:
        - None: None을 반환합니다.
        """
        async with db.begin():
            answer = await self.answer_repository.find_answer(db, answer_id)

            if answer is None:
                raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Answer not found")

            user = await self.user_repository.find_user(db, {"username": user.username})

            await self.vote_repository.vote_answer(user, answer)