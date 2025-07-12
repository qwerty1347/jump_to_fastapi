from common.response import success_response, error_response


class OcrService():
    def __init__(self):
        pass

    async def handle_ocr(self):
        try:
            return success_response()
        except Exception as e:
            return error_response(message=str(e))