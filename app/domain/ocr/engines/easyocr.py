import easyocr

from app.domain.ocr.engines.base_engine import BaseEngine


class EasyOcr(BaseEngine):
    def __init__(self):
        self.easyocr = easyocr.Reader(['ko', 'en'])

    async def recognize(self, file_path: str) -> dict:
        return self.convert_to_json(self.easyocr.readtext(file_path))


    def convert_to_json(self, ocr_result) -> dict:
        result = {
            "images": []
        }

        for poly, text, confidence in ocr_result:
            bounding_poly: list[list[int]] = [[int(vertex[0]), int(vertex[1])] for vertex in poly]
            result["images"].append({
                "boundingPoly": bounding_poly,
                "text": text,
                "confidence": float(confidence)
            })

        return result