from abc import ABC, abstractmethod


class BaseEngine(ABC):
    def __init__(self):
        pass

    @abstractmethod
    async def recognize(self, file_path: str) -> dict:
        """
        이미지 파일에서 텍스트를 추출하는 함수

        매개변수:
        - file_path (str): OCR을 수행할 이미지 파일의 경로

        반환값:
        - dict: 이미지에서 추출된 텍스트 목록
        """
        pass


    @abstractmethod
    def convert_to_json(self, ocr_result) -> dict:
        """
        OCR 결과를 JSON 형식으로 변환하는 함수

        매개변수:
        - ocr_result (list): OCR 수행 결과

        반환값:
        - dict: OCR 결과를 JSON으로 변환한 결과
        """
        pass