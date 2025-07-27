from pydantic import BaseModel

from app.domain.ocr.schemas.enum import OcrEngine


class OcrRequest(BaseModel):
    engine: OcrEngine