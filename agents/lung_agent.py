from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List
from schemas.models import LungDiagnosis

load_dotenv()



llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

structured_llm = llm.with_structured_output(
    LungDiagnosis
)

def lung_agent(symptoms):

    prompt = f"""
    You are a pulmonologist.

    Analyze:
    {symptoms}

    Return:
    - lung condition
    - severity
    - recommendations
    """

    response = structured_llm.invoke(prompt)

    return response