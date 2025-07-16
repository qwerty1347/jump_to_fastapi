from paddleocr import PaddleOCR

from app.domain.ocr.engines.base_engine import BaseEngine


class PaddleOcr(BaseEngine):
    def __init__(self):
        self.paddleocr = PaddleOCR(lang='korean', use_angle_cls=False)

    async def recognize(self, file_path: str) -> dict:
        return self.convert_to_json(self.paddleocr.ocr(file_path))


    def convert_to_json(self, ocr_result) -> dict:
        result = {
            "images": []
        }

        polys = ocr_result[0].get("rec_polys", [])
        texts = ocr_result[0].get("rec_texts", [])
        confidences = ocr_result[0].get("rec_scores", [])

        for poly, text, confidence in zip(polys, texts, confidences):
            bounding_poly = poly.tolist() if hasattr(poly, "tolist") else poly
            result["images"].append({
                "boundingPoly": bounding_poly,
                "text": text,
                "confidence": float(confidence)
            })

        return result