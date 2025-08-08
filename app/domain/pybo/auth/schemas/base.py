from pydantic import BaseModel, ConfigDict


class AuthBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)