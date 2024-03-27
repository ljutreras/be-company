from typing import List, Optional
from fastapi import HTTPException
from pydantic import BaseModel, validator
from uuid import uuid4

class BotModel(BaseModel):
    actions: List[str]
    descriptions: List[str]
    responses: List[str]
    unique_id: Optional[str] = ''

    @validator('unique_id')
    def set_unique_id(cls, value):
        return str(uuid4()) if value == '' else value

    @validator('actions')
    def validate_actions(cls, value, values, **kwargs):
        responses = values.get('responses')
        if responses and len(value) != len(responses):
            raise HTTPException(status_code=400, detail="Number of actions, descriptions and responses must be equal")
        return value

    @validator('descriptions')
    def validate_responses(cls, value, values, **kwargs):
        actions = values.get('actions')
        if actions and len(actions) != len(value):
            raise HTTPException(status_code=400, detail="Number of actions, descriptions and responses must be equal")
        return value
    
    @validator('responses')
    def validate_responses(cls, value, values, **kwargs):
        actions = values.get('actions')
        if actions and len(actions) != len(value):
            raise HTTPException(status_code=400, detail="Number of actions, descriptions and responses must be equal")
        return value