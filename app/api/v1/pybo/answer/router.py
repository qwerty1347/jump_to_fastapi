from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.answer.dependencies.dependency import parse_answer_create_form, parse_answer_query, parse_answer_update_form_payload, parse_answer_update_json_payload
from app.domain.pybo.answer.schemas.request import AnswerQueryRequest, AnswerCreateRequest, AnswerUpdateRequest
from app.domain.pybo.answer.schemas.response import AnswerResponse
from app.domain.pybo.answer.services.service import AnswerService
from app.domain.pybo.auth.dependencies.dependency import get_current_user
from common.constants.route import RouteConstants
from common.response import success_response
from databases.mysql.session import get_mysql_session


router = APIRouter(prefix=RouteConstants.ANSWER_PREFIX, tags=[RouteConstants.ANSWER_TAG])
answer_service = AnswerService()


@router.get('/')
async def get_answers(
    query_dto: AnswerQueryRequest = Depends(parse_answer_query),
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    Answer 리스트를 가져오는 엔드포인트

    매개변수:
    - query_dto (AnswerQueryRequest): Answer 리스트를 가져올 때의
        옵션을 정의하는 데이터를 전달합니다.
    - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    반환값:
    - JSONResponse: Answer 리스트가 포함된 성공 응답을 반환합니다.
    """
    try:
        response = await answer_service.get_answers(db, query_dto)
        return success_response(jsonable_encoder(response))

    except Exception as e:
        raise e


@router.get('/{answer_id}', response_model=AnswerResponse)
async def find_answer(
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
    try:
        response = await answer_service.find_answer(db, answer_id)
        return success_response(jsonable_encoder(response))
    
    except HTTPException as e:
        raise e

    except Exception as e:
        raise e


@router.post('/form')
async def create_answer(
    create_dto: AnswerCreateRequest = Depends(parse_answer_create_form),
    user = Depends(get_current_user),
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    Answer 하나를 생성하는 엔드포인트 (폼 데이터)

    매개변수:
    - create_dto (AnswerCreateRequest): Answer 생성을 위한 폼 데이터를 전달합니다.
    - user (UserItemResponse): 사용자의 정보를 포함하는 UserItemResponse를 전달합니다.
    - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    반환값:
    - JSONResponse: 생성된 Answer 하나가 포함된 성공 응답을 반환합니다.
    """
    try:
        response = await answer_service.create_answer(db, create_dto)
        return success_response(jsonable_encoder(response), HTTPStatus.CREATED)

    except Exception as e:
        raise e


@router.post('/json')
async def create_answer(
    create_dto: AnswerCreateRequest,
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    Answer를 생성하는 엔드포인트 (JSON 데이터)

    Args:
        create_dto (AnswerCreateRequest): Answer 생성을 위한 JSON 데이터를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: 생성된 Answer 하나가 포함된 성공 응답을 반환합니다.
    """
    try:
        response = await answer_service.create_answer(db, create_dto)
        return success_response(jsonable_encoder(response), HTTPStatus.CREATED)
        
    except Exception as e:
        raise e


@router.put('/form/{answer_id}')
async def update_answer(
    answer_id: int = Path(...),
    update_dto: AnswerUpdateRequest = Depends(parse_answer_update_form_payload),
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    Answer 하나를 수정하는 엔드포인트 (폼 데이터)

    Args:
        answer_id (int): Answer 하나의 고유 ID를 전달합니다.
        update_dto (AnswerUpdateRequest): Answer 수정을 위한 폼 데이터를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: 수정된 Answer 하나가 포함된 성공 응답을 반환합니다.
    """
    try:
        response = await answer_service.update_answer(db, answer_id, update_dto)
        return success_response(jsonable_encoder(response))
    
    except Exception as e:
        raise e


@router.put('/json/{answer_id}')
async def update_answer(
    answer_id: int = Path(...),
    update_dto: AnswerUpdateRequest = Depends(parse_answer_update_json_payload),
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    Answer를 수정하는 엔드포인트 (JSON 데이터)

    Args:
        answer_id (int): Answer 하나의 고유 ID를 전달합니다.
        update_dto (AnswerUpdateRequest): Answer 수정을 위한 JSON 데이터를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: 수정된 Answer 하나가 포함된 성공 응답을 반환합니다.
    """
    try:
        response = await answer_service.update_answer(db, answer_id, update_dto)
        return success_response(jsonable_encoder(response))

    except Exception as e:
        raise e


@router.delete('/{answer_id}')
async def delete_answer(
    answer_id: int = Path(...),
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    Answer 하나를 삭제하는 엔드포인트

    Args:
        answer_id (int): Answer 하나의 고유 ID를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: 삭제된 Answer 하나가 포함된 성공 응답을 반환합니다.
    """
    try:
        response = await answer_service.delete_answer(db, answer_id)
        return success_response(jsonable_encoder(response))
        
    except Exception as e:
        raise e