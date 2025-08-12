from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.login.dependencies.dependency import parse_login_form
from app.domain.pybo.login.schemas.request import LoginRequest
from app.domain.pybo.login.schemas.response import LoginTokenResponse
from app.domain.pybo.login.services.service import LoginService
from common.constants.route import RouteConstants
from common.utils.response import success_response
from databases.mysql.session import get_mysql_session


router = APIRouter(prefix=RouteConstants.LOGIN_PREFIX, tags=[RouteConstants.LOGIN_TAG])
login_service = LoginService()


@router.post('/form', response_model=LoginTokenResponse)
async def index(
    login_dto: LoginRequest = Depends(parse_login_form),
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    username과 password로 access_token을 발급하는 엔드포인트

    매개변수:
    - login_dto (LoginRequest): User 인증을 위한 폼 데이터를 전달합니다.
    - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    반환값:
    - JSONResponse: 생성된 access_token이 포함된 성공 응답을 반환합니다.
    """
    response = await login_service.login_for_access_token(db, login_dto)
    return success_response(jsonable_encoder(response))


@router.post('/json', response_model=LoginTokenResponse)
async def index(
    login_dto: LoginRequest,
    db: AsyncSession = Depends(get_mysql_session)
) -> JSONResponse:
    """
    username과 password로 access_token을 발급하는 엔드포인트 (JSON 데이터)

    매개변수:
    - login_dto (LoginRequest): User 인증을 위한 JSON 데이터를 전달합니다.
    - db (AsyncSession): 비동기 데이터베이스 세션을 사용합니다.

    반환값:
    - JSONResponse: 생성된 access_token이 포함된 성공 응답을 반환합니다.
    """
    response = await login_service.login_for_access_token(db, login_dto)
    return success_response(jsonable_encoder(response))