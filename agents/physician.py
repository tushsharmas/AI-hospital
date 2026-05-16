from langchain_groq import ChatGroq
from schemas.models import Diagnosis
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

structured_llm = llm.with_structured_output(Diagnosis)

def physician_agent(symptoms: str):

    prompt = f"""
    You are a physician AI.

    Patient symptoms:
    {symptoms}

    Return diagnosis information.
    """

    response = structured_llm.invoke(prompt)

    return response