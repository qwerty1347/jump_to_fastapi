from fastapi import APIRouter, Depends, Path
from fastapi.responses import JSONResponse
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.routers.v1.answer.dependencies.dependency import parse_answer_create_form
from app.domain.pybo.routers.v1.answer.dtos.request import AnswerRequest
from app.domain.pybo.routers.v1.answer.dtos.response import AnswerResponse
from app.domain.pybo.routers.v1.answer.services.service import AnswerService
from databases.mysql.session import get_mysql_session


router = APIRouter(prefix="/answer", tags=["Answer"])
answer_service = AnswerService()


@router.get('/', response_model=AnswerResponse)
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


@router.get('/{answer_id}', response_model=AnswerResponse)
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


@router.post('/form', response_model=AnswerResponse)
async def create_answer(
    create_dto: AnswerRequest = Depends(parse_answer_create_form),
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    Answer를 생성하는 엔드포인트 (폼 데이터)

    Args:
        create_dto (AnswerRequest): Answer 생성을 위한 폼 데이터를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: 생성된 Answer 하나가 포함된 성공 응답을 반환합니다.
    """
    return await answer_service.create_answer(db, create_dto)


@router.post('/json')
async def create_answer(
    create_dto: AnswerRequest,
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    Answer를 생성하는 엔드포인트 (JSON 데이터)

    Args:
        create_dto (AnswerRequest): Answer 생성을 위한 JSON 데이터를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: 생성된 Answer 하나가 포함된 성공 응답을 반환합니다.
    """
    return await answer_service.create_answer(db, create_dto)
