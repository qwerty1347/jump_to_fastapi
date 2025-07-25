from fastapi import APIRouter

from app.api.v1.pybo.question.router import router as question_router
from app.api.v1.pybo.answer.router import router as answer_router
from app.api.v1.pybo.user.router import router as user_router


router = APIRouter(prefix="/pybo")
router.include_router(question_router)
router.include_router(answer_router)
router.include_router(user_router)


@router.get('/')
async def index():
    return {"message": "Hello pybo"}
