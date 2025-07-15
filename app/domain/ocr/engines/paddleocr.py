from paddleocr import PaddleOCR

from app.domain.ocr.engines.base_engine import BaseEngine


class PaddleOcr(BaseEngine):
    def __init__(self):
        self.paddleocr = PaddleOCR(lang='korean', use_angle_cls=False)

    async def recognize(self, file_path: str) -> list[str]:
        result = self.paddleocr.ocr(file_path)

        if result and isinstance(result, list) and isinstance(result[0], dict):
            return result[0].get('rec_texts', [])