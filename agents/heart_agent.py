from langchain_groq import ChatGroq
from dotenv import load_dotenv
from tools.blood_pressure_analyzer import blood_pressure_analyzer
from tools.chest_pain_analyzer import chest_pain_analyzer
from tools.heart_rate_checker import heart_rate_checker
from langgraph.prebuilt import create_react_agent
from tools.severity_checker import severity_checker
from tools.drug_checker import drug_interaction_checker

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

tools = [
    severity_checker,
    drug_interaction_checker,
    heart_rate_checker,
    blood_pressure_analyzer,
    chest_pain_analyzer
]

agent = create_react_agent(
    llm,
    tools=tools
)


def heart_agent(symptoms):

    response = agent.invoke({
        "messages": [
            (
                "user",
                f"""
                You are an expert cardiologist.

                Analyze these symptoms carefully:

                {symptoms}

                Use tools whenever needed.

                Provide:
                - possible cardiac condition
                - severity
                - recommendations
                """
            )
        ]
    })



    print(response)
    
    return response