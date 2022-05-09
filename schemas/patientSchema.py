from pydantic import BaseModel
from datetime import date

class PatientCreateInput(BaseModel):
    name: str
    birth_date: date