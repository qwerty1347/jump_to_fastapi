from fastapi import APIRouter, Depends, Path
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.answer.services.service import AnswerService
from app.domain.pybo.question.dependencies.dependency import parse_question_create_form, parse_question_update_form_payload, parse_question_update_json_payload, parse_questions_query
from app.domain.pybo.question.schemas.request import QuestionCreateRequest, QuestionUpdateRequest, QuestionQueryRequest
from app.domain.pybo.question.schemas.response import QuestionResponse
from app.domain.pybo.question.services.service import QuestionService
from common.constants.route import RouteConstants
from databases.mysql.session import get_mysql_session


router = APIRouter(prefix=RouteConstants.QUESTION_PREFIX, tags=[RouteConstants.QUESTION_TAG])
question_service = QuestionService()
answer_service = AnswerService()


@router.get('/')
async def get_questions(
    query_dto: QuestionQueryRequest = Depends(parse_questions_query),
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
     Question 리스트를 가져오는 엔드포인트

     매개변수:
     - query_dto (QuestionQueryRequest): Question 리스트를 가져올 때의
         옵션을 정의하는 데이터를 전달합니다.
     - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

     반환값:
     - JSONResponse: Question 리스트가 포함된 성공 응답을 반환합니다.
     """
    return await question_service.get_questions(db, query_dto)


@router.get('/{question_id}', response_model=QuestionResponse)
async def find_question(
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
    return await question_service.find_question(db, question_id)


@router.post('/form', response_model=QuestionResponse)
async def create_question(
    create_dto: QuestionCreateRequest = Depends(parse_question_create_form),
    db: AsyncSession = Depends(get_mysql_session),
) -> JSONResponse:
    """
    Question을 생성하는 엔드포인트

    Args:
        create_dto (QuestionCreateRequest): Question 생성을 위한 폼 데이터를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: 생성된 Question 하나가 포함된 성공 응답을 반환합니다.
    """
    return await question_service.create_question(db, create_dto)


@router.post('/json', response_model=QuestionResponse)
async def create_question(
    create_dto: QuestionCreateRequest,
    db: AsyncSession = Depends(get_mysql_session),
) -> JSONResponse:
    """
    Question을 생성하는 엔드포인트

    Args:
        create_dto (QuestionCreateRequest): Question 생성을 위한 JSON 데이터를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: 생성된 Question 하나가 포함된 성공 응답을 반환합니다.
    """
    return await question_service.create_question(db, create_dto)


@router.put('/form/{question_id}', response_model=QuestionResponse)
async def update_question_by_question_id(
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
    return await question_service.update_question_by_question_id(db, question_id, update_dto)


@router.put('/json/{question_id}', response_model=QuestionResponse)
async def update_question_by_question_id_by_json(
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
    return await question_service.update_question_by_question_id(db, question_id, update_dto)


@router.delete('/{question_id}', response_model=QuestionResponse)
async def delete_question_by_question_id(
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
    return await question_service.delete_question_by_question_id(db, question_id)


@router.get('/{question_id}/answer')
async def get_answers_by_question_id(
    question_id: int = Path(...),
    db: AsyncSession = Depends(get_mysql_session)
):
    return await answer_service.get_answers_by_question_id(db, question_id)
