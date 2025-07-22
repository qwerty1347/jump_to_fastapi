from fastapi import APIRouter, Depends, Path
from fastapi.responses import JSONResponse
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.routers.v1.answer.services.service import AnswerService
from databases.mysql.session import get_mysql_session


router = APIRouter(prefix="/answer", tags=["Answer"])
answer_service = AnswerService()


@router.get('/')
async def get_answers(
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    Answer 리스트를 가져오는 엔드포인트

    Args:
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: Answer 리스트가 포함된 성공 응답을 반환합니다.
    """
    return await answer_service.get_answers(db)


@router.get('/{answer_id}')
async def get_answer(
    answer_id: int = Path(...),
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    Answer 하나를 가져오는 엔드포인트

    Args:
        answer_id (int): Answer 하나의 고유 ID를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: Answer 하나가 포함된 성공 응답을 반환합니다.
    """
    return await answer_service.get_answer(db, answer_id)