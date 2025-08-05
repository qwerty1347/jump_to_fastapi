from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.user.dependencies.dependency import parse_user_create_form_payload, parse_user_query
from app.domain.pybo.user.schemas.request import UserCreateRequest, UserQueryRequest
from app.domain.pybo.user.schemas.response import UserResponse
from app.domain.pybo.user.services.service import UserService
from databases.mysql.session import get_mysql_session


router = APIRouter(prefix="/user", tags=["User"])
user_service = UserService()


@router.post('/form', response_model=UserResponse)
async def create_user(
    create_dto: UserCreateRequest = Depends(parse_user_create_form_payload),
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    User을 생성하는 엔드포인트 (폼 데이터)

    Args:
        create_dto (UserCreateRequest): User 생성을 위한 폼 데이터를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: 생성된 User 하나가 포함된 성공 응답을 반환합니다.
    """
    return await user_service.create_user(db, create_dto)


@router.post('/json', response_model=UserResponse)
async def create_user(
    create_dto: UserCreateRequest,
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    User을 생성하는 엔드포인트 (JSON 데이터)

    Args:
        create_dto (UserCreateRequest): User 생성을 위한 JSON 데이터를 전달합니다.
        db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    Returns:
        JSONResponse: 생성된 User 하나가 포함된 성공 응답을 반환합니다.
    """
    return await user_service.create_user(db, create_dto)


@router.get('/')
async def get_user(
    query_dto: UserQueryRequest = Depends(parse_user_query),
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
     User 하나를 가져오는 엔드포인트

     Args:
         query_dto (UserQueryRequest): User 하나를 가져올 때의
             옵션을 정의하는 데이터를 전달합니다.
         db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

     Returns:
         JSONResponse: 가져온 User 하나가 포함된 성공 응답을 반환합니다.
     """
    return await user_service.get_user(db, query_dto)