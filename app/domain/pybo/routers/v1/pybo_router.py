from fastapi import APIRouter


router = APIRouter(prefix="/pybo", tags=["pybo"])

@router.get('/')
async def index():
    return {"message": "Hello pybo"}
