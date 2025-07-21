from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.routers.v1.question.dependencies.create_dependency import get_question_form_data
from app.domain.pybo.routers.v1.question.dtos.request import QuestionRequest
from app.domain.pybo.routers.v1.question.dtos.response import QuestionListResponse
from app.domain.pybo.routers.v1.question.services.service import QuestionService
from databases.mysql.session import get_mysql_session


router = APIRouter(prefix="/question")
question_service = QuestionService()


@router.get('/', response_model=QuestionListResponse)
async def get_question_list(db: AsyncSession = Depends(get_mysql_session)) -> JSONResponse:
    """
    Question 리스트를 가져오는 엔드포인트

    Args:
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: Question 리스트가 포함된 성공 응답을 반환합니다.
    """

    return await question_service.get_question_list(db)


@router.get('/{question_id}', response_model=QuestionListResponse)
async def get_question_item(
    question_id: int,
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    Question 하나를 가져오는 엔드포인트

    Args:
        question_id (int): Question 하나의 고유 ID를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: Question 하나가 포함된 성공 응답을 반환합니다.
    """
    return await question_service.get_question_item(db, question_id)


@router.post('/form', response_model=QuestionListResponse)
async def create_item_by_form_data(
    form_data: QuestionRequest = Depends(get_question_form_data),
    db: AsyncSession = Depends(get_mysql_session),
) -> JSONResponse:
    """
    Question을 생성하는 엔드포인트

    Args:
        form_data (QuestionRequest): Question 생성을 위한 폼 데이터를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: 생성된 Question 하나가 포함된 성공 응답을 반환합니다.
    """
    return await question_service.create_item_by_form_data(db, form_data)


@router.post('/json', response_model=QuestionListResponse)
async def create_item_by_json(
    json_data: QuestionRequest,
    db: AsyncSession = Depends(get_mysql_session),
) -> JSONResponse:
    """
    Question을 생성하는 엔드포인트

    Args:
        json_data (QuestionRequest): Question 생성을 위한 JSON 데이터를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: 생성된 Question 하나가 포함된 성공 응답을 반환합니다.
    """
    return await question_service.create_item_by_json(db, json_data)