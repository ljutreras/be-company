from html import escape
from pydantic import BaseModel, validator

class AskBot(BaseModel):
    message: str

    @validator('message')
    def validate_message(cls, value):
        value = escape(value[:200])
        return value
