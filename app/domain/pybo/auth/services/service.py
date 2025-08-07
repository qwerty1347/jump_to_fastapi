from datetime import datetime, timedelta, timezone
from jose import jwt

from config.settings import settings 


class AuthService():
    def __init__(self):
        pass
    
    
    @staticmethod
    def create_access_token(username: str) -> dict[str, str]:
        """사용자 인증 정보를 확인하여 access_token을 생성하는 동기 메서드
        
        매개변수:
        - username (str): 사용자의 username을 전달합니다.
        
        반환값:
        - dict[str, str]: 생성된 access_token이 포함된 성공 응답을 반환합니다.
        """
        data = {
            "sub": username,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=settings.PYBO_JWT_EXPIRE_MINUTES)
        }
        
        return {
            "access_token": jwt.encode(data, settings.PYBO_JWT_SECRET_KEY, algorithm=settings.PYBO_JWT_ALGORITHM),
            "token_type": "bearer",
            "username": username
        }