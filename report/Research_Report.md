# AI Researcher Take-Home Assessment

## Part 1: Research & Model Evaluation

---

# 1. Introduction

This project evaluates the suitability of frontier closed-source and open-source Large Language Models (LLMs) for autonomous AI agent workflows.

The study compares GPT-5 (OpenAI) and Llama 3.3 70B (Meta) in the context of an autonomous logistics rerouting system. Rather than evaluating only the final output, this research focuses on the complete decision trajectory, including intermediate reasoning, tool usage, workflow execution, and recovery behavior.

---

# 2. Problem Statement

Logistics disruptions such as carrier failures and weather delays often require manual intervention. This proof-of-concept demonstrates how multiple AI agents can autonomously analyze shipment telemetry, evaluate available carriers, and execute a rerouting decision.

Business Goal:

Develop a lightweight multi-agent workflow capable of autonomously responding to shipment disruptions while minimizing delivery delays.

---

# 3. Models Compared

## Closed-Source Model

**GPT-5 (OpenAI)**

Strengths

- Excellent reasoning
- Strong tool usage
- Reliable structured outputs
- Superior error recovery
- Production-ready

Limitations

- Higher inference cost
- Vendor lock-in
- Requires API access

---

## Open-Source Model

**Llama 3.3 70B (Meta)**

Strengths

- Self-hosted deployment
- Lower operational cost
- Customizable
- Better privacy control

Limitations

- Slightly weaker reasoning
- Additional engineering effort
- Infrastructure management required

---

# 4. Evaluation Methodology

Instead of comparing only the final answer, a trajectory-based evaluation methodology was used.

Evaluation criteria included:

- Intermediate reasoning quality
- Tool-calling capability
- Decision consistency
- Error recovery
- Multi-step planning
- Workflow completion

This approach provides greater visibility into how AI agents make decisions throughout the workflow.

---

# 5. Agent Workflow

Telemetry Agent

↓

Decision Agent

↓

Execution Agent

Responsibilities:

Telemetry Agent

- Detect shipment delay
- Extract shipment information

Decision Agent

- Compare carriers
- Evaluate ETA
- Evaluate cost
- Evaluate reliability

Execution Agent

- Execute reroute
- Generate confirmation
- Update shipment status

---

# 6. Demonstration Benchmark Results

> **Note:** The following results are illustrative demonstration results created for this assessment and are not official benchmark scores.

| Metric | GPT-5 | Llama 3.3 70B |
|--------|-------|---------------|
| Reasoning | Excellent | Good |
| Tool Calling | Excellent | Good |
| Error Recovery | Excellent | Moderate |
| Multi-step Planning | Excellent | Good |
| Latency | Medium | Fast |
| Cost | High | Low |
| Production Readiness | Very High | Good |

---

# 7. Technical Trade-offs

### GPT-5

Advantages

- Highest reasoning quality
- Reliable structured outputs
- Better handling of complex workflows
- Lower implementation effort

Disadvantages

- Higher API cost
- Vendor dependency
- Internet connectivity required

---

### Llama 3.3

Advantages

- Lower operational cost
- Self-hosted deployment
- Greater customization
- Better data privacy

Disadvantages

- More infrastructure management
- Lower reasoning performance in complex workflows
- Additional engineering effort

---

# 8. Emerging AI Agent Techniques

The following techniques improve autonomous AI systems:

- LangGraph graph-based workflows
- Multi-agent orchestration
- Stateful execution
- Tool calling
- Memory integration
- Human-in-the-loop review
- Self-healing workflows
- Process monitoring
- Process mining
- Retrieval-Augmented Generation (RAG)
- Structured outputs

These techniques improve reliability, maintainability, and production readiness.

---

# 9. Product Recommendation

GPT-5 remains the stronger choice for production environments requiring maximum reasoning capability and reliability.

Llama 3.3 is a compelling alternative when deployment flexibility, cost efficiency, and data privacy are primary requirements.

For enterprise logistics systems, a hybrid strategy is recommended:

- GPT-5 handles complex decision-making.
- Llama 3.3 manages routine workflows and cost-sensitive tasks.

This balances performance, operational cost, and scalability.

---

# 10. Conclusion

This project demonstrates that trajectory-based evaluation provides deeper insights into AI agent behavior than evaluating only final outputs.

The LangGraph multi-agent proof-of-concept successfully illustrates how autonomous AI workflows can detect shipment disruptions, evaluate alternatives, and execute logistics rerouting with minimal human intervention.

Future enhancements include integrating real-time carrier APIs, human approval checkpoints, Retrieval-Augmented Generation (RAG), and production monitoring for enterprise deployment.
