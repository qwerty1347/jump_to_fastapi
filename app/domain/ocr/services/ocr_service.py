import easyocr

from fastapi import UploadFile

from common.helpers.file import delete_file, save_file
from common.response import success_response, error_response


class OcrService():
    def __init__(self):
        pass

    async def handle_ocr(self, file:UploadFile):
        try:
            file_path = await save_file(file)
            ocr_result = await self.do_easy_ocr(str(file_path))
            print(ocr_result)
            return success_response()

        except Exception as e:
            return error_response(message=str(e))

        finally:
            await delete_file(file_path)


    async def do_easy_ocr(self, file_path) -> list[str]:
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
