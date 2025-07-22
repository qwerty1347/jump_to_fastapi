from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.models.answer import Answer


class AnswerRepository:
    def __init__(self):
        pass


    async def get_answers_by_question_id(self, db: AsyncSession, question_id: int) -> List[Answer]:
        """
        특정 질문 ID에 해당하는 answer 목록을 가져오는 비동기 메서드

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - question_id (int): 특정 질문의 고유 ID를 전달합니다.

        반환값:
        - List[Answer]: 특정 질문에 해당하는 answer 목록이 포함된 성공 응답을 반환합니다.
        """
        result = await db.execute(select(Answer).where(Answer.question_id == question_id).order_by(Answer.created_at.desc()))
        answers = result.scalars().all()

        return answers


    async def get_answers(self, db: AsyncSession) -> List[Answer]:
        """
        answer 리스트를 가져오는 비동기 메서드

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

        반환값:
        - List[Answer]: answer 리스트가 포함된 성공 응답을 반환합니다.
        """
        result = await db.execute(select(Answer).order_by(Answer.created_at.desc()))
        answers = result.scalars().all()

        return answers


    async def get_answer(self, db: AsyncSession, answer_id: int) -> Answer:
        """
        answer 하나를 가져오는 비동기 메서드

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - answer_id (int): answer 하나의 고유 ID를 전달합니다.

        반환값:
        - Answer: answer 하나가 포함된 성공 응답을 반환합니다.
        """
        result = await db.execute(select(Answer).where(Answer.id == answer_id))
        answer = result.scalars().first()

        return answer