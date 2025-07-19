from fastapi import APIRouter

from app.domain.pybo.routers.v1.question.router import router as question_router


router = APIRouter(prefix="/pybo", tags=["pybo"])
router.include_router(question_router)


@router.get('/')
async def index():
    return {"message": "Hello pybo"}
