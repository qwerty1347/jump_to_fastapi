from fastapi import APIRouter


router = APIRouter(prefix="/answer", tags=["Answer"])


@router.get('/')
async def index():
    return {"message": "Hello answer"}