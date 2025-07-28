from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.user.dependencies.dependency import parse_user_create_form_payload
from app.domain.pybo.user.schemas.request import UserCreateRequest
from databases.mysql.session import get_mysql_session


router = APIRouter(prefix="/user", tags=["User"])


@router.get('/')
async def index():
    return {"message": "Hello pybo-user"}


@router.post('/form')
async def create_user(
    create_dto: UserCreateRequest = Depends(parse_user_create_form_payload),
    db: AsyncSession = Depends(get_mysql_session)
):
    return {"message": "Hello create-user"}