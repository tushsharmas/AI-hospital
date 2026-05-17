<div align="center">

```
██╗  ██╗ ██████╗ ███████╗██████╗ ██╗████████╗ █████╗ ██╗
██║  ██║██╔═══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔══██╗██║
███████║██║   ██║███████╗██████╔╝██║   ██║   ███████║██║
██╔══██║██║   ██║╚════██║██╔═══╝ ██║   ██║   ██╔══██║██║
██║  ██║╚██████╔╝███████║██║     ██║   ██║   ██║  ██║███████╗
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
```

# 🏥 AI Hospital — Multi-Agent Medical Diagnostic System

> **An intelligent, multi-agent AI system that simulates a real hospital workflow — from intake to specialist diagnosis.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-🦜-1C3C3C?style=for-the-badge)](https://langchain.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-🕸️-orange?style=for-the-badge)](https://langgraph.dev)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-F55036?style=for-the-badge)](https://groq.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 🧠 What Is This?

**AI Hospital** is a production-inspired, multi-agent medical diagnostic system that mimics how a real hospital triages and routes patients. You describe your symptoms — the system thinks, routes, and responds like a team of expert doctors.

Under the hood, an **Orchestrator AI** acts as the senior physician at intake. It analyses your symptoms, decides if a general physician is sufficient, or routes you to the most appropriate **specialist agent** — each powered by a fine-tuned LLM prompt and optional tool use.

---

## 🏗️ System Architecture

```
                        ┌─────────────────────────┐
                        │      Patient Input       │
                        │   (Symptoms / History)   │
                        └────────────┬────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────┐
                        │    🧑‍⚕️ Orchestrator AI    │
                        │   (Senior Physician)     │
                        │                         │
                        │  • Triage & Assess       │
                        │  • Route Decision        │
                        │  • Safety Screening      │
                        └─────┬───────────┬────────┘
                              │           │
               needs_specialist=False     needs_specialist=True
                              │           │
                              ▼           ▼
                   ┌──────────────┐  ┌──────────────────────────────┐
                   │  General     │  │       Specialist Routing      │
                   │  Physician   │  │                              │
                   │  Response    │  │  ❤️ Heart    🫁 Lungs         │
                   └──────────────┘  │  🦴 Bones    👁️ Eyes          │
                                     │  🤰 Pregnancy 🫘 Kidneys     │
                                     └──────────────────────────────┘
```

---

## 🤖 The Agent Team

| Agent | Role | Specialty | Approach |
|-------|------|-----------|----------|
| 🧑‍⚕️ **Orchestrator** | Senior Physician | Triage & Routing | Structured output with routing logic |
| ❤️ **Heart Agent** | Cardiologist | Cardiac Symptoms | ReAct agent with medical tools |
| 🫁 **Lung Agent** | Pulmonologist | Respiratory Issues | Structured diagnosis output |
| 🫘 **Kidney Agent** | Nephrologist | Renal Conditions | Structured diagnosis output |
| 👁️ **Eye Agent** | Ophthalmologist | Vision & Eye Disorders | Structured diagnosis output |
| 🤰 **Pregnancy Agent** | Gynecologist | Maternal & Reproductive Health | Structured diagnosis output |

---

## 🛠️ Heart Agent — Tool-Augmented Reasoning

The **Heart Agent** is the most advanced agent in the system. Unlike others, it uses a **LangGraph ReAct loop** with real medical tools:

```
Heart Agent (ReAct)
│
├── 🔧 blood_pressure_analyzer     → Interprets BP readings
├── 🔧 chest_pain_analyzer         → Classifies chest pain patterns
├── 🔧 heart_rate_checker          → Evaluates heart rate data
├── 🔧 severity_checker            → Scores overall severity
└── 🔧 drug_interaction_checker    → Flags dangerous drug combos
```

This means the heart agent can *reason step-by-step*, call tools, observe results, and refine its diagnosis — just like a real cardiologist would.

---

## 📁 Project Structure

```
ai-hospital/
│
├── orchestrator.py             # Master routing agent (senior physician)
│
├── agents/
│   ├── heart_agent.py          # ❤️  ReAct agent with tools
│   ├── lung_agent.py           # 🫁  Structured pulmonologist
│   ├── kidney_agent.py         # 🫘  Structured nephrologist
│   ├── eye_agent.py            # 👁️  Structured ophthalmologist
│   └── pregnancy_agent.py      # 🤰  Structured gynecologist
│
├── tools/
│   ├── blood_pressure_analyzer.py
│   ├── chest_pain_analyzer.py
│   ├── heart_rate_checker.py
│   ├── severity_checker.py
│   └── drug_interaction_checker.py
│
├── schemas/
│   ├── models.py               # Pydantic output schemas per specialist
│   └── routing.py              # RoutingDecision schema for orchestrator
│
├── .env                        # API keys (GROQ_API_KEY)
└── requirements.txt
```

---

## ⚡ Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-hospital.git
cd ai-hospital
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> 🔑 Get your free API key at [console.groq.com](https://console.groq.com)

### 4. Run the system

```python
from orchestrator import orchestrator_agent
from heart_agent import heart_agent

# Step 1: Triage with orchestrator
symptoms = "I have severe chest pain radiating to my left arm, shortness of breath, and sweating."
routing = orchestrator_agent(symptoms)

print(f"Needs Specialist: {routing.needs_specialist}")
print(f"Routing to: {routing.specialist}")

# Step 2: Send to specialist
if routing.needs_specialist and routing.specialist == "heart":
    diagnosis = heart_agent(symptoms)
    print(diagnosis)
```

---

## 🔄 How It Works — Step by Step

```
1. Patient describes symptoms
         │
         ▼
2. Orchestrator analyses symptoms using LLaMA 3.3 70B
   → Returns structured RoutingDecision:
     { needs_specialist, specialist, reason, assessment, recommendations }
         │
         ├── needs_specialist = False → General advice returned
         │
         └── needs_specialist = True
                  │
                  ▼
3. Appropriate specialist agent invoked
   → Each agent has a specialist-specific prompt + schema
   → Heart agent additionally uses ReAct + tools
         │
         ▼
4. Structured diagnosis returned
   { condition, severity, recommendations }
```

---

## 🧬 Pydantic Schemas

Every diagnosis is **type-safe and structured** using Pydantic v2:

```python
# Example: HeartDiagnosis schema
class HeartDiagnosis(BaseModel):
    condition: str          # Possible cardiac condition
    severity: str           # low / moderate / high / critical
    recommendations: List[str]  # Actionable next steps
```

The Orchestrator uses:

```python
class RoutingDecision(BaseModel):
    needs_specialist: bool
    specialist: Optional[str]   # "heart" | "lungs" | "kidney" | ...
    reason: str
    initial_assessment: str
    possible_condition: str
    recommendations: List[str]
```

---

## 🧰 Tech Stack

| Component | Technology |
|-----------|------------|
| LLM | LLaMA 3.3 70B via Groq |
| Agent Framework | LangChain + LangGraph |
| Structured Output | Pydantic v2 |
| ReAct Loop | LangGraph `create_react_agent` |
| Environment | `python-dotenv` |

---

## 🚨 Medical Disclaimer

> ⚠️ **This project is for educational and research purposes only.**
> It is NOT a substitute for professional medical advice, diagnosis, or treatment.
> Always consult a qualified healthcare provider for any medical concerns.

---

## 🤝 Contributing

Contributions are welcome! Here are some ideas to extend the system:

- [ ] Add a **Dermatology** or **Neurology** specialist agent
- [ ] Build a **Streamlit / FastAPI** frontend for the system
- [ ] Add **patient history memory** using LangGraph state
- [ ] Integrate **RAG** with medical databases (PubMed, UpToDate)
- [ ] Add **voice input** via Whisper API

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

**Built with 🧠 LangChain · LangGraph · Groq · LLaMA 3.3**

*"Bringing multi-agent intelligence to the clinic."*

</div>
