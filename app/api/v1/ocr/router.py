from fastapi import APIRouter, Depends, File, UploadFile

from app.domain.ocr.dependencies.dependency import parse_ocr_request
from app.domain.ocr.schemas.request import OcrRequest
from app.domain.ocr.services.service import OcrService
from app.domain.ocr.validators.file import validate_upload_file
from common.constants.route import RouteConstants


router = APIRouter(prefix=RouteConstants.OCR_PREFIX, tags=[RouteConstants.OCR_TAG])

ocr_service = OcrService()


@router.post('/')
async def ocr(
    file: UploadFile = File(...),
    ocr_dto: OcrRequest = Depends(parse_ocr_request)
):
    validate_upload_file(file)
    return await ocr_service.handle_ocr(file, ocr_dto.engine.value)