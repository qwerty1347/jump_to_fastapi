from fastapi import APIRouter

from app.domain.ocr.routers.v1.router import router as ocr_router
from common.constants.route import API_V1_PREFIX


api_v1_router = APIRouter(prefix=API_V1_PREFIX)

api_v1_router.include_router(ocr_router)