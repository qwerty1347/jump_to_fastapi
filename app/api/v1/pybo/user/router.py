from fastapi import APIRouter


router = APIRouter(prefix="/user", tags=["User"])


@router.get('/')
async def index():
    return {"message": "Hello pybo-user"}


@router.post('/form')
async def create_user():
    return {"message": "Hello create-user"}