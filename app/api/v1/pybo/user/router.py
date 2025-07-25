from fastapi import APIRouter


router = APIRouter(prefix="/user", tags=["User"])

@router.get('/')
async def index():
    return {"message": "Hello user"}