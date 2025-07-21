from openai import BaseModel
from pydantic import ConfigDict


class QuestionBase(BaseModel):
    id: int
    subject: str
    content: str

    model_config = ConfigDict(from_attributes=True)