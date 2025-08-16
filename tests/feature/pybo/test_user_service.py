import pytest

from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.pybo.user.schemas.request import UserCreateRequest
from app.domain.pybo.user.schemas.response import UserItemResponse
from app.domain.pybo.user.services.service import UserService


@pytest.mark.asyncio
class TestUserService:
    async def async_setup(self):
        self.service = UserService()


    async def test_create_user(self, db: AsyncSession):
        await self.async_setup()
        create_dto = UserCreateRequest(
            username="test_user2",
            password1="test_password2",
            password2="test_password2",
            email="test_email2"
        )
        result = await self.service.create_user(db, create_dto)

        assert isinstance(result, UserItemResponse)