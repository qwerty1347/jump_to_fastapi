from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.question.models.question import Question
from app.domain.pybo.user.models.user import User


class VoteRepository():
    def __init__(self):
        pass
    
    
    async def vote_question(self, user: User, question: Question):
        question.voter.append(user)