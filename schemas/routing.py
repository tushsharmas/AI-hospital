from pydantic import BaseModel
from typing import Optional, List

class RoutingDecision(BaseModel):

    needs_specialist: bool

    specialty: Optional[str]

    reason: str

    initial_assessment: str

    possible_condition: Optional[str]

    recommendations: List[str]