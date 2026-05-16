from langchain.tools import tool


@tool
def blood_pressure_analyzer(bp: str) -> str:
    """
    Analyze blood pressure readings.
    """

    try:

        systolic, diastolic = map(
            int,
            bp.split("/")
        )

        if systolic >= 180 or diastolic >= 120:
            return "Hypertensive crisis"

        elif systolic >= 140 or diastolic >= 90:
            return "High blood pressure"

        elif systolic < 90:
            return "Low blood pressure"

        return "Blood pressure normal"

    except:
        return "Invalid blood pressure format"