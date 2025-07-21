from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.routers.v1.question.dtos.response import QuestionListResponse
from app.domain.pybo.routers.v1.question.services.service import QuestionService
from databases.mysql.session import get_mysql_session


router = APIRouter(prefix="/question")
question_service = QuestionService()


@router.get(
    '/list',
    response_model=QuestionListResponse
)
async def get_question_list(db: AsyncSession = Depends(get_mysql_session)):
    return await question_service.get_question_list(db)