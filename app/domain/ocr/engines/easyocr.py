import easyocr

from app.domain.ocr.engines.base_engine import BaseEngine


class EasyOcr(BaseEngine):
    def __init__(self):
        pass

    async def recognize(self, file_path: str):
        """
        이미지 파일에서 텍스트를 추출하는 함수

        매개변수:
        - file_path (str): OCR을 수행할 이미지 파일의 경로

        반환값:
        - list[str]: 이미지에서 추출된 텍스트 목록
        """
        reader = easyocr.Reader(['ko', 'en'], gpu=True)
        results = reader.readtext(file_path)
        ocr_texts = []

        for bbox, text, prob in results:
            ocr_texts.append(text.strip())

        return ocr_texts