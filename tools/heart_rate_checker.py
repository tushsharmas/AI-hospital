from langchain.tools import tool


@tool
def heart_rate_checker(rate: str) -> str:
    """
    Analyze heart rate.
    """

    try:

        rate = int(rate)

        if rate > 120:
            return "Tachycardia"

        if rate < 50:
            return "Bradycardia"

        return "Heart rate normal"

    except:
        return "Invalid heart rate"