from langgraph.graph import StateGraph, END

from graph.state import HospitalState

from agents.orchestrator import orchestrator_agent
from agents.heart_agent import heart_agent
from agents.bone_agent import bone_agent
from agents.eye_agent import eye_agent
from agents.kidney_agent import kidney_agent
from agents.lung_agent import lung_agent
from agents.pregnancy_agent import pregnancy_agent


# -----------------------------
# ORCHESTRATOR NODE
# -----------------------------

def orchestrator_node(state):

    decision = orchestrator_agent(
        state["user_input"]
    )

    return {
        "routing_decision": decision
    }


# -----------------------------
# HEART NODE
# -----------------------------

def heart_node(state):

    result = heart_agent(
        state["user_input"]
    )

    return {
        "specialist_response": result
    }


# -----------------------------
# BONE NODE
# -----------------------------

def bone_node(state):

    result = bone_agent(
        state["user_input"]
    )

    return {
        "specialist_response": result
    }


# -----------------------------
# EYE NODE
# -----------------------------

def eye_node(state):

    result = eye_agent(
        state["user_input"]
    )

    return {
        "specialist_response": result
    }


# -----------------------------
# KIDNEY NODE
# -----------------------------

def kidney_node(state):

    result = kidney_agent(
        state["user_input"]
    )

    return {
        "specialist_response": result
    }


# -----------------------------
# LUNG NODE
# -----------------------------

def lung_node(state):

    result = lung_agent(
        state["user_input"]
    )

    return {
        "specialist_response": result
    }


# -----------------------------
# PREGNANCY NODE
# -----------------------------

def pregnancy_node(state):

    result = pregnancy_agent(
        state["user_input"]
    )

    return {
        "specialist_response": result
    }


# -----------------------------
# ROUTING LOGIC
# -----------------------------

def route_specialist(state):

    decision = state["routing_decision"]

    if not decision.needs_specialist:
        return END

    if decision.specialty == "heart":
        return "heart_agent"

    elif decision.specialty == "bones":
        return "bone_agent"

    elif decision.specialty == "eyes":
        return "eye_agent"

    elif decision.specialty == "kidney":
        return "kidney_agent"

    elif decision.specialty == "lungs":
        return "lung_agent"

    elif decision.specialty == "pregnancy":
        return "pregnancy_agent"

    return END


# -----------------------------
# BUILD GRAPH
# -----------------------------

builder = StateGraph(HospitalState)


# Add Nodes

builder.add_node(
    "orchestrator",
    orchestrator_node
)

builder.add_node(
    "heart_agent",
    heart_node
)

builder.add_node(
    "bone_agent",
    bone_node
)

builder.add_node(
    "eye_agent",
    eye_node
)

builder.add_node(
    "kidney_agent",
    kidney_node
)

builder.add_node(
    "lung_agent",
    lung_node
)

builder.add_node(
    "pregnancy_agent",
    pregnancy_node
)


# Entry Point

builder.set_entry_point(
    "orchestrator"
)


# Conditional Routing

builder.add_conditional_edges(
    "orchestrator",
    route_specialist
)


# END Connections

builder.add_edge("heart_agent", END)

builder.add_edge("bone_agent", END)

builder.add_edge("eye_agent", END)

builder.add_edge("kidney_agent", END)

builder.add_edge("lung_agent", END)

builder.add_edge("pregnancy_agent", END)


# Compile Graph

graph = builder.compile()