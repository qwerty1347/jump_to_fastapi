from fastapi import APIRouter

from app.domain.ocr.routers.v1.router import router as ocr_router
from app.domain.pybo.routers.v1.router import router as pybo_router
from common.constants.route import RouteConstants


api_v1_router = APIRouter(prefix=RouteConstants.API_V1_PREFIX)

api_v1_router.include_router(ocr_router)
api_v1_router.include_router(pybo_router)