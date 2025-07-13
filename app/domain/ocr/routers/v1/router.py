from fastapi import APIRouter, File, UploadFile

from app.domain.ocr.services.ocr_service import OcrService
from app.domain.ocr.validators.file import validate_upload_file
from common.constants.route import OCR_PREFIX, OCR_TAG


router = APIRouter(prefix=OCR_PREFIX, tags=[OCR_TAG])

ocr_service = OcrService()


@router.get('/')
async def index():
    return {"message": "Hello OCR"}


@router.post('/')
async def ocr(file:UploadFile = File(...)):
    validate_upload_file(file)
    return await ocr_service.handle_ocr(file)