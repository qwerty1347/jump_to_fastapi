from openai import BaseModel
from pydantic import ConfigDict


class QuestionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True, orm_mode=True)