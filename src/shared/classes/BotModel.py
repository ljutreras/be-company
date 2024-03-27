from typing import Optional
from pydantic import BaseModel, validator
from uuid import uuid4

class BotModel(BaseModel):
    actions: list[str]
    responses: list[str]
    unique_id: Optional[str] = ''

    @validator('unique_id')
    def set_unique_id(cls, value):
        return str(uuid4()) if value == '' else value