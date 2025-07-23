from typing import List
from sqlalchemy import delete, select, update
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


    async def create_answer(self, db: AsyncSession, create_dto: dict) -> Answer:
        """
        answer 하나를 생성하는 비동기 메서드

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - create_dto (dict): answer 생성을 위한 폼 데이터를 전달합니다.

        반환값:
        - Answer: 생성된 answer 하나가 포함된 성공 응답을 반환합니다.
        """
        answer = Answer(**create_dto)
        db.add(answer)
        await db.flush()
        await db.refresh(answer)
        return answer


    async def update_answer(self, db: AsyncSession, answer_id: int, update_dto: dict) -> int:
        """
        answer 하나를 수정하는 비동기 메서드

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - answer_id (int): answer 하나의 고유 ID를 전달합니다.
        - update_dto (dict): answer 수정을 위한 폼 데이터를 전달합니다.

        반환값:
        - int: 수정된 answer의 개수가 포함된 성공 응답을 반환합니다.
        """
        result = await db.execute(update(Answer).where(Answer.id == answer_id).values(**update_dto))
        return result.rowcount


    async def delete_answer(self, db: AsyncSession, answer_id: int) -> int:
        """
        answer 하나를 삭제하는 비동기 메서드

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - answer_id (int): answer 하나의 고유 ID를 전달합니다.

        반환값:
        - int: 삭제된 answer의 개수가 포함된 성공 응답을 반환합니다.
        """
        result = await db.execute(delete(Answer).where(Answer.id == answer_id))
        return result.rowcount