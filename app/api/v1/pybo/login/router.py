from fastapi import APIRouter


router = APIRouter(prefix="/user/login")


@router.get('/')
async def index():
    return {"message": "Hello login"}
