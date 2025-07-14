import easyocr

from app.domain.ocr.engines.base_engine import BaseEngine


class EasyOcr(BaseEngine):
    def __init__(self):
        self.easyocr = easyocr.Reader(['ko', 'en'])

    async def recognize(self, file_path: str) -> list[str]:
        """
        이미지 파일에서 텍스트를 추출하는 함수

        매개변수:
        - file_path (str): OCR을 수행할 이미지 파일의 경로

        반환값:
        - list[str]: 이미지에서 추출된 텍스트 목록
        """
        result = self.easyocr.readtext(file_path)
        ocr_texts = []

        for bbox, text, prob in result:
            ocr_texts.append(text.strip())

        return ocr_texts