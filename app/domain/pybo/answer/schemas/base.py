from pydantic import BaseModel, ConfigDict


class AnswerBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class AnswerAffectResponse(BaseModel):
    result: bool
    code: int