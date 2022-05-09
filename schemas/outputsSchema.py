from pydantic import BaseModel
from typing import List

class StandardOutput(BaseModel):
    message: str

class ErrorOutput(BaseModel):
    detail: str
