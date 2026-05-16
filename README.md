AI Hospital 🏥🤖
An intelligent multi-agent AI hospital system where specialized medical AI agents collaborate to analyze patient symptoms and route cases to the correct medical specialist.
Built using:
langchain.com⁠�
langchain.com⁠�
groq.com⁠�
Python
Structured AI Outputs with Pydantic
🚀 Overview
This project simulates a smart AI-powered hospital environment.
Instead of using one large AI model for every medical problem, the system uses:
An Orchestrator AI Doctor
Multiple Specialist AI Agents
The orchestrator first analyzes patient symptoms and decides:
whether a general physician can handle the case
or whether the patient should be routed to a specialist doctor agent
Each specialist agent focuses only on its medical domain.
🧠 Architecture
Plain text
Patient Symptoms
        ↓
Hospital Orchestrator AI
        ↓
 ┌───────────────┬───────────────┬───────────────┐
 ↓               ↓               ↓
Heart Agent    Eye Agent      Kidney Agent
 ↓               ↓               ↓
Specialized Medical Analysis
👨‍⚕️ Available Specialist Agents
❤️ Heart Specialist Agent
Handles:
chest pain
blood pressure
heart rate
palpitations
cardiac symptoms
Features:
Tool calling
Severity analysis
Drug interaction checking
Chest pain analyzer
Blood pressure analyzer
👁️ Eye Specialist Agent
Handles:
blurry vision
eye pain
redness
retina-related issues
visual disturbances
Provides:
eye condition analysis
severity estimation
recommendations
🩺 Kidney Specialist Agent
Handles:
urinary issues
kidney pain
swelling
renal-related symptoms
Provides:
kidney condition analysis
severity estimation
recommendations
🦴 Bone Specialist Agent
Handles:
fractures
joint pain
spine problems
orthopedic conditions
muscle issues
Provides:
orthopedic analysis
severity estimation
recommendations
🏥 Orchestrator Agent
The orchestrator acts as the hospital’s senior physician.
Responsibilities:
Analyze symptoms
Decide if specialist care is needed
Route patients safely
Provide preliminary assessment
Avoid unnecessary escalation
Prioritize medical safety
The orchestrator can route patients to:
Heart specialist
Bone specialist
Eye specialist
Kidney specialist
Lung specialist
Pregnancy specialist
⚙️ Technologies Used
Python
LangChain
LangGraph
Groq LLMs
Pydantic
Structured Outputs
Multi-Agent Architecture
AI Tool Calling
📂 Project Structure
Plain text
project/
│
├── orchestrator.py
├── heart_agent.py
├── eye_agent.py
├── kidney_agent.py
├── bone_agent.py
│
├── tools/
│   ├── blood_pressure_analyzer.py
│   ├── chest_pain_analyzer.py
│   ├── heart_rate_checker.py
│   ├── severity_checker.py
│   └── drug_checker.py
│
├── schemas/
│   ├── models.py
│   └── routing.py
│
└── .env
🔑 Environment Variables
Create a .env file:
Environment
GROQ_API_KEY=your_api_key_here
Get API key from:
console.groq.com⁠�
📦 Installation
Clone the repository:
Bash
git clone https://github.com/yourusername/yourrepo.git
Install dependencies:
Bash
pip install -r requirements.txt
Run the project:
Bash
python main.py
🧪 Example Workflow
Patient Input
Plain text
I have chest pain and shortness of breath.
Orchestrator Decision
Plain text
Specialist Needed: True
Selected Specialist: Heart Agent
Heart Agent Analysis
Plain text
Possible Condition:
Angina or cardiac stress

Severity:
Moderate to high

Recommendations:
Immediate cardiac evaluation recommended.
🛡️ Medical Safety Principles
This project:
avoids definitive diagnosis claims
provides preliminary assessments only
prioritizes emergency escalation when necessary
encourages professional medical consultation
⚠️ Disclaimer
This project is for:
educational purposes
AI research
multi-agent system experimentation
It is NOT a replacement for:
licensed doctors
hospitals
emergency medical services
Always seek professional medical advice for real health concerns.
🌟 Future Improvements
Voice-based patient interaction
Medical memory system
RAG with medical knowledge base
ECG/X-ray analysis
Appointment booking
Full hospital dashboard
Electronic Health Records (EHR)
Multi-specialist collaboration
Emergency triage system
🤝 Contributions
Contributions are welcome.
Feel free to:
improve agents
add specialists
enhance safety systems
optimize prompts
build frontend/dashboard
📜 License
MIT License
⭐ Support
If you like this project:
Star the repository
Fork the project
Contribute improvements
👨‍💻 Author
Built with AI + Multi-Agent Systems ❤️
