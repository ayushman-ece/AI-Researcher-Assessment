# AI Researcher Take-Home Assessment

## Project Overview

This project demonstrates a lightweight multi-agent AI workflow for autonomous logistics rerouting using LangGraph.

The system automatically responds to shipment delays by analyzing telemetry data, evaluating alternative carriers, and selecting the best rerouting option.

---

## Business Problem

Logistics companies often experience shipment delays due to weather conditions, carrier failures, or operational issues.

Instead of relying on manual intervention, this proof-of-concept demonstrates how AI agents can autonomously:

- Detect shipment delays
- Analyze the disruption
- Evaluate alternative carriers
- Select the optimal carrier
- Execute the rerouting process
- Notify the logistics system

---

## Technology Stack

- Python 3.11+
- LangGraph
- LangChain
- OpenAI (Optional)
- python-dotenv

---

## Project Structure

```
AI-Researcher-Assessment/
│
├── app.py
├── agents.py
├── workflow.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
│
├── report/
│   └── Research_Report.md
│
└── presentation/
```

---

## AI Workflow

```
Delay Alert
      │
      ▼
Telemetry Agent
      │
      ▼
Decision Agent
      │
      ▼
Execution Agent
      │
      ▼
Shipment Successfully Rerouted
```

---

## Agent Responsibilities

### 1. Telemetry Agent

- Detect shipment delay
- Read shipment information
- Determine delay severity

### 2. Decision Agent

- Evaluate available carriers
- Compare ETA
- Compare cost
- Compare reliability
- Select the best carrier

### 3. Execution Agent

- Execute rerouting
- Update shipment
- Generate confirmation

---

## Installation

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Copy

```
.env.example
```

to

```
.env
```

If you have an OpenAI API Key

```
OPENAI_API_KEY=your_key
USE_MOCK=false
```

Otherwise keep

```
USE_MOCK=true
```

The project works without any API keys.

---

## Run

```bash
python app.py
```

---

## Expected Output

The workflow will

- Detect shipment delay
- Evaluate carrier options
- Select the best carrier
- Execute rerouting
- Display workflow summary

---

## AI Tool Usage Decision Log

AI tools were used only to accelerate development and documentation.

- ChatGPT was used for brainstorming architecture, improving code quality, generating documentation, and refining the research report.
- Claude was used to assist in structuring the presentation deck.
- Final workflow design, evaluation methodology, architectural decisions, and implementation were reviewed and finalized manually.

---

## Future Improvements

- Real-time carrier APIs
- Database integration
- Human approval workflow
- Retrieval-Augmented Generation (RAG)
- Multi-modal telemetry inputs
- Real-time monitoring dashboard

---

## Author

AI Researcher Intern Take-Home Assessment