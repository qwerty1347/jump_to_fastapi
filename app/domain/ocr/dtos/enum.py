from enum import Enum

from common.constants.ocr import OcrConstants


class OcrEngine(str, Enum):
    easyocr = OcrConstants.EASY_OCR
    paddleocr = OcrConstants.PADDLE_OCR
    clovaocr = OcrConstants.CLOVA_OCR