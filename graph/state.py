from typing import TypedDict, Optional

from schemas.routing import RoutingDecision


class HospitalState(TypedDict):

    user_input: str

    routing_decision: Optional[RoutingDecision]

    specialist_response: Optional[dict]

    final_response: Optional[str]