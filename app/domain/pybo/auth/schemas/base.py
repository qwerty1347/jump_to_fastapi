from openai import BaseModel
from pydantic import ConfigDict


class AuthBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)