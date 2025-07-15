from pydantic import BaseModel

from app.domain.ocr.dtos.enum import OcrEngine


class OcrRequest(BaseModel):
    engine: OcrEngine