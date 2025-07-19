from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.models.question import Question


class QuestionRepository:
    def __init__(self):
        pass

    async def get_question_list(self, db: AsyncSession) -> List[Question]:
        result = await db.execute(select(Question).order_by(Question.created_at.desc()))

        questions = result.scalars().all()

        return questions