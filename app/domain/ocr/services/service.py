from fastapi import UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.domain.ocr.schemas.response import OcrResponse
from app.domain.ocr.modules.module import OcrModule
from common.response import success_response, error_response


class OcrService():
    def __init__(self):
        pass

    async def handle_ocr(self, file: UploadFile, engine: str) -> JSONResponse:
        """
        OCR 엔진을 동작하여 업로드된 이미지의 텍스트를 추출하는 함수

        매개변수:
        - file (UploadFile): 업로드된 이미지 파일
        - engine (str): 사용할 OCR 엔진

        반환값:
        - JSONResponse: 추출된 텍스트 목록을 담은 JSON 응답
        """
        try:
            ocr_engine = OcrModule(engine)
            ocr_result = await ocr_engine.recognize(file)

            response = OcrResponse(
                ocr_result = ocr_result
            )

            return success_response(jsonable_encoder(response))

        except Exception as e:
            return error_response(message=str(e))