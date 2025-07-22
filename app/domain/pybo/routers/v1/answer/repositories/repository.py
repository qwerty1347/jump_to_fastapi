from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.models.answer import Answer


class AnswerRepository:
    def __init__(self):
        pass


    async def get_answers_by_question_id(self, db: AsyncSession, question_id: int):
        result = await db.execute(select(Answer).where(Answer.question_id == question_id).order_by(Answer.created_at.desc()))
        answers = result.scalars().all()

        return answers