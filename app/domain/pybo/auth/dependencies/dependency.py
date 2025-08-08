from http import HTTPStatus
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from app.domain.pybo.auth.services.service import AuthService
from app.domain.pybo.user.schemas.response import UserItemResponse
from common.response import error_response


auth_service = AuthService()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/pybo/user/login/json")



async def get_current_user(token: str = Depends(oauth2_scheme)):
    """토큰을 확인하여 사용자 정보를 가져오는 비동기 메서드
    
    매개변수:
    - token (str): 토큰을 전달합니다.
    
    반환값:
    - dict[str, str]: 사용자 정보가 포함된 성공 응답을 반환합니다.
    """
    try:
        return await auth_service.validate_access_token(token)
    
    except JWTError:
        return error_response(code=HTTPStatus.UNAUTHORIZED, message="Could not validate credentials")
    
    except HTTPException as e:
        raise e
    
    except Exception as e:
        return error_response(message=str(e))    