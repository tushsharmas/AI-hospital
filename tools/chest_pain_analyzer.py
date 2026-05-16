from langchain.tools import tool


@tool
def chest_pain_analyzer(symptoms: str) -> str:
    """
    Analyze chest pain symptoms.
    """

    symptoms = symptoms.lower()

    if "sweating" in symptoms and "chest pain" in symptoms:
        return "Possible cardiac emergency"

    if "left arm" in symptoms:
        return "Possible heart attack symptoms"

    return "Needs cardiology evaluation"