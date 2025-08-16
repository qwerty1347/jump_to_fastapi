import pytest

from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.login.schemas.request import LoginRequest
from app.domain.pybo.login.services.service import LoginService


@pytest.mark.asyncio
class TestLoginService:
    async def async_setup(self):
        self.service = LoginService()


    async def test_login_for_access_token(self, db: AsyncSession):
        await self.async_setup()
        login_dto = LoginRequest(username="test1", password="test1")
        access_token = await self.service.login_for_access_token(db, login_dto)

        assert isinstance(access_token, dict)


    async def test_is_authenticated_user(self, db: AsyncSession):
        await self.async_setup()
        login_dto = LoginRequest(username="test1", password="test1")
        result = await self.service.is_authenticated_user(db, login_dto)

        assert result is None
