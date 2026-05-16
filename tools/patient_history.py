from langchain.tools import tool


@tool
def patient_history_tool(patient_id: str) -> str:
    """
    Retrieve patient medical history.
    """

    fake_database = {

        "101": "Hypertension and diabetes",

        "102": "Asthma history"
    }

    return fake_database.get(
        patient_id,
        "No history found"
    )