from fastapi import APIRouter, Depends, Path
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.routers.v1.question.dependencies.dependency import parse_question_create_form, parse_question_update_form_payload, parse_question_update_json_payload
from app.domain.pybo.routers.v1.question.dtos.request import QuestionRequest, QuestionUpdateRequest
from app.domain.pybo.routers.v1.question.dtos.response import QuestionResponse
from app.domain.pybo.routers.v1.question.services.service import QuestionService
from databases.mysql.session import get_mysql_session


router = APIRouter(prefix="/question", tags=["Question"])
question_service = QuestionService()


@router.get('/', response_model=QuestionResponse)
async def get_question_list(db: AsyncSession = Depends(get_mysql_session)) -> JSONResponse:
    """
    Question 리스트를 가져오는 엔드포인트

    Args:
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: Question 리스트가 포함된 성공 응답을 반환합니다.
    """

    return await question_service.get_question_list(db)


@router.get('/{question_id}', response_model=QuestionResponse)
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


@router.post('/form', response_model=QuestionResponse)
async def create_item(
    form_data: QuestionRequest = Depends(parse_question_create_form),
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
    return await question_service.create_item(db, form_data)


@router.post('/json', response_model=QuestionResponse)
async def create_item(
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
    return await question_service.create_item(db, json_data)


@router.put('/form/{question_id}', response_model=QuestionResponse)
async def update_item(
    question_id: int = Path(...),
    update_dto: QuestionUpdateRequest = Depends(parse_question_update_form_payload),
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    Question을 수정하는 엔드포인트

    Args:
        question_id (int): Question 하나의 고유 ID를 전달합니다.
        update_dto (QuestionUpdateRequest): Question 수정을 위한 폼 데이터를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: 수정된 Question 하나가 포함된 성공 응답을 반환합니다.
    """
    return await question_service.update_item(db, question_id, update_dto)


@router.put('/json/{question_id}', response_model=QuestionResponse)
async def update_item_by_json(
    question_id: int = Path(...),
    update_dto: QuestionUpdateRequest = Depends(parse_question_update_json_payload),
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    Question을 수정하는 엔드포인트

    Args:
        question_id (int): Question 하나의 고유 ID를 전달합니다.
        update_dto (QuestionUpdateRequest): Question 수정을 위한 JSON 데이터를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: 수정된 Question 하나가 포함된 성공 응답을 반환합니다.
    """
    return await question_service.update_item(db, question_id, update_dto)


@router.delete('/{question_id}', response_model=QuestionResponse)
async def delete_item(
    question_id: int = Path(...),
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    Question을 삭제하는 엔드포인트

    Args:
        question_id (int): Question 하나의 고유 ID를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: 삭제된 Question의 개수가 포함된 성공 응답을 반환합니다.
    """
    return await question_service.delete_item(db, question_id)