from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from http import HTTPStatus

from common.response import error_response


async def validate_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    """
    RequestValidationError 예외 처리 함수

    RequestValidationError 예외가 발생하면
    JSONResponse를 반환하여 클라이언트에게 에러 메시지를 전송
    """
    errors = exc.errors()
    error_message = "; ".join([f"field {error['loc']} - {error['msg']}" for error in errors])
    return error_response(HTTPStatus.UNPROCESSABLE_ENTITY, error_message)


async def http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    """
    StarletteHTTPException 예외 처리 함수

    StarletteHTTPException 예외가 발생하면
    JSONResponse를 반환하여 클라이언트에게 에러 메시지를 전송
    """
    return error_response(exc.status_code, str(exc.detail))


def register_exception_handlers(app):
    """
    FastAPI 애플리케이션에 예외 처리 핸들러를 등록하는 함수

    RequestValidationError, StarletteHTTPException 예외 처리 핸들러를 등록
    """
    app.add_exception_handler(RequestValidationError, validate_exception_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)