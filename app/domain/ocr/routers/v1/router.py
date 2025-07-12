from fastapi import APIRouter, File, UploadFile

from app.domain.ocr.services.ocr_service import OcrService
from app.domain.ocr.validators.file_validator import validate_upload_file


router = APIRouter(prefix="/ocr", tags=["OCR"])

ocr_service = OcrService()


@router.get('/')
async def index():
    return {"message": "Hello OCR"}


@router.post('/')
async def ocr(file:UploadFile = File(...)):
    validate_upload_file(file)
    return await ocr_service.handle_ocr()