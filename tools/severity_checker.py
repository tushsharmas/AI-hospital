from langchain.tools import tool


@tool
def severity_checker(symptoms: str) -> str:
    """
    Analyze symptoms and estimate severity level.
    """

    symptoms = symptoms.lower()

    emergency_keywords = [
        "chest pain",
        "difficulty breathing",
        "stroke",
        "unconscious",
        "severe bleeding"
    ]

    for keyword in emergency_keywords:

        if keyword in symptoms:
            return "emergency"

    moderate_keywords = [
        "fever",
        "vomiting",
        "cough"
    ]

    for keyword in moderate_keywords:

        if keyword in symptoms:
            return "moderate"

    return "low"