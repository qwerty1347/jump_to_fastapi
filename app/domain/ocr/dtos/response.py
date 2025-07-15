from typing import List
from pydantic import BaseModel


class OcrResponse(BaseModel):
       ocr_result: List[str]