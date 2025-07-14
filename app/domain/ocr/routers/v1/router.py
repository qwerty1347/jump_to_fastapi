from fastapi import APIRouter, File, Form, UploadFile

from app.domain.ocr.services.ocr_service import OcrService
from app.domain.ocr.validators.file import validate_upload_file
from common.constants.route import RouteConstants



router = APIRouter(prefix=RouteConstants.OCR_PREFIX, tags=[RouteConstants.OCR_TAG])

ocr_service = OcrService()


@router.post('/')
async def ocr(
    file: UploadFile = File(...),
    engine: str = Form(...),
):
    validate_upload_file(file)
    return await ocr_service.handle_ocr(file, engine)