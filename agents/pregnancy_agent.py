from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List
from schemas.models import PregnancyDiagnosis

load_dotenv()



llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

structured_llm = llm.with_structured_output(
    PregnancyDiagnosis
)

def pregnancy_agent(symptoms):

    prompt = f"""
    You are a gynecologist.

    Analyze:
    {symptoms}

    Return:
    - pregnancy/reproductive condition
    - severity
    - recommendations
    """

    response = structured_llm.invoke(prompt)

    return response