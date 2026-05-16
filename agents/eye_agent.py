from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List
from schemas.models import EyeDiagnosis

load_dotenv()


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

structured_llm = llm.with_structured_output(
    EyeDiagnosis
)

def eye_agent(symptoms):

    prompt = f"""
    You are an ophthalmologist.

    Analyze:
    {symptoms}

    Return:
    - eye condition
    - severity
    - recommendations
    """

    response = structured_llm.invoke(prompt)

    return response