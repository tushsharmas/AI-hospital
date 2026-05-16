from pydantic import BaseModel
from typing import Optional
from typing import List




class HeartDiagnosis(BaseModel):

    condition: str

    severity: str

    recommendations: List[str]    

class BoneDiagnosis(BaseModel):

    condition: str

    severity: str

    recommendations: List[str]    

class EyeDiagnosis(BaseModel):

    condition: str

    severity: str

    recommendations: List[str]

class KidneyDiagnosis(BaseModel):

    condition: str

    severity: str

    recommendations: List[str]    

class LungDiagnosis(BaseModel):

    condition: str

    severity: str

    recommendations: List[str]    

class PregnancyDiagnosis(BaseModel):

    condition: str

    severity: str

    recommendations: List[str]

