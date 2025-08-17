import pytest

from app.domain.pybo.auth.services.service import AuthService


@pytest.mark.asyncio
class TestAuthService:
    async def async_setup(self):
        self.service = AuthService()


    async def test_verify_access_token(self):
        await self.async_setup()
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0MiIsImV4cCI6MTc1NTI0ODE3NH0.IszZSQA3n7--RKkvgk5hr0gp97UQt37IceGAKPpOBpA"
        username = await self.service.validate_access_token(token)

        assert isinstance(username, str)