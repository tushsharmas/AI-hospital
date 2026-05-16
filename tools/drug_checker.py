from langchain.tools import tool


@tool
def drug_interaction_checker(drugs: str) -> str:
    """
    Check possible dangerous drug interactions.
    """

    drugs = drugs.lower()

    if "warfarin" in drugs and "aspirin" in drugs:
        return "Warning: increased bleeding risk"

    return "No major interaction detected"