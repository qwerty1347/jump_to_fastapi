from fastapi.routing import APIRouter

from app.api.v1 import api_v1_router


def get_api_routers() -> list[APIRouter]:
    return [
        api_v1_router,
    ]