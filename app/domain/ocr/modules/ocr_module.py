from fastapi import UploadFile

from app.domain.ocr.engines.clovaocr import ClovaOcr
from app.domain.ocr.engines.easyocr import EasyOcr
from app.domain.ocr.engines.paddleocr import PaddleOcr
from common.constants.ocr import OcrConstants


class OcrModule:
    OCR_ENGINES = {
        OcrConstants.EASY_OCR: EasyOcr,
        OcrConstants.PADDLE_OCR: PaddleOcr,
        OcrConstants.CLOVA_OCR: ClovaOcr,
    }

    def __init__(self, engine: str):
        self.engine = engine
        pass


    def _get_engine_instance(self):
        ocr_engine = self.OCR_ENGINES.get(self.engine)

        if ocr_engine is None:
            raise Exception(f"지원하지 않는 엔진입니다: {self.engine}")

        return ocr_engine()


    async def recognize(self, file: UploadFile):
        ocr_engine = self._get_engine_instance()
        return await ocr_engine.recognize(file)
