from fastapi import UploadFile

from app.domain.ocr.modules.ocr_module import OcrModule
from common.helpers.file import delete_file, save_file
from common.response import success_response, error_response


class OcrService():
    def __init__(self):
        pass

    async def handle_ocr(self, file: UploadFile, engine: str):
        try:
            file_path = await save_file(file)
            ocr_engine = OcrModule(engine)
            ocr_result = await ocr_engine.recognize(str(file_path))

            print(ocr_result)
            return success_response()

        except Exception as e:
            return error_response(message=str(e))

        finally:
            await delete_file(file_path)
