from fastapi import APIRouter


router = APIRouter(prefix="/ocr", tags=["OCR"])

@router.get('/')
async def index():
    return {"message": "Hello OCR"}