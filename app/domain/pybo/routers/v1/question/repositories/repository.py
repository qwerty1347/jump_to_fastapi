from typing import List
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.models.question import Question


class QuestionRepository:
    def __init__(self):
        pass

    async def get_question_list(self, db: AsyncSession) -> List[Question]:
        """
        Question 리스트를 가져오는 비동기 메서드

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

        반환값:
        - List[Question]: Question 리스트가 포함된 성공 응답을 반환합니다.
        """
        result = await db.execute(select(Question).order_by(Question.created_at.desc()))
        questions = result.scalars().all()

        return questions


    async def get_question_item(self, db:AsyncSession, question_id: int) -> Question | None:
        """
        Question 하나를 가져오는 비동기 메서드

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - question_id (int): Question 하나의 고유 ID를 전달합니다.

        반환값:
        - Question | None: Question 하나가 포함된 성공 응답을 반환하거나, 실패 시 None을 반환합니다.
        """
        result = await db.execute(select(Question).where(Question.id == question_id))
        question = result.scalars().first()

        return question


    async def create_item(self, db: AsyncSession, item: dict) -> Question:
        """
        Question을 생성하는 비동기 메서드

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - item (dict): Question 생성을 위한 데이터를 전달합니다.

        반환값:
        - Question: 생성된 Question 하나가 포함된 성공 응답을 반환합니다.
        """
        question = Question(**item)
        db.add(question)
        await db.flush()
        await db.refresh(question)
        return question


    async def update_item(self, db: AsyncSession, question_id: int, form_data: dict) -> int:
        """
        Question을 수정하는 비동기 메서드

        매개변수:
        - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.
        - question_id (int): Question 하나의 고유 ID를 전달합니다.
        - form_data (dict): Question 수정을 위한 폼 데이터를 전달합니다.

        반환값:
        - int: 수정된 Question의 개수가 포함된 성공 응답을 반환합니다.
        """
        result = await db.execute(update(Question).where(Question.id == question_id).values(**form_data))
        return result.rowcount