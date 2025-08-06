from pydantic import BaseModel, ConfigDict


class LoginBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)