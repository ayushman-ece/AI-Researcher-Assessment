from typing import TypedDict, Dict, Any
from config import Config

try:
    from langchain_openai import ChatOpenAI
except ImportError:
    ChatOpenAI = None


class WorkflowState(TypedDict):
    shipment: Dict[str, Any]
    telemetry: Dict[str, Any]
    decision: Dict[str, Any]
    execution: Dict[str, Any]


# -----------------------------
# Optional GPT-5 Support
# -----------------------------
def ask_gpt(prompt: str):

    if (
        Config.USE_MOCK
        or not Config.OPENAI_API_KEY
        or ChatOpenAI is None
    ):
        return None

    llm = ChatOpenAI(
        model=Config.MODEL_NAME,
        api_key=Config.OPENAI_API_KEY,
        temperature=0,
    )

    return llm.invoke(prompt).content


# -----------------------------
# Telemetry Agent
# -----------------------------
def telemetry_agent(state: WorkflowState):

    shipment = state["shipment"]

    telemetry = {
        "status": "Delay Detected",
        "delay_reason": shipment["delay_reason"],
        "delay_hours": shipment["expected_delay_hours"],
        "severity": "High" if shipment["expected_delay_hours"] >= 5 else "Medium",
    }

    print("\n" + "=" * 60)
    print("🚚 TELEMETRY AGENT")
    print("=" * 60)

    print(f"Shipment ID : {shipment['shipment_id']}")
    print(f"Origin      : {shipment['origin']}")
    print(f"Destination : {shipment['destination']}")
    print(f"Reason      : {telemetry['delay_reason']}")
    print(f"Delay       : {telemetry['delay_hours']} Hours")
    print(f"Severity    : {telemetry['severity']}")

    state["telemetry"] = telemetry
    return state


# -----------------------------
# Decision Agent
# -----------------------------
def decision_agent(state: WorkflowState):

    carriers = Config.ALTERNATIVE_CARRIERS

    print("\n" + "=" * 60)
    print("🧠 DECISION AGENT")
    print("=" * 60)

    prompt = f"""
Choose the best carrier.

Carriers:
{carriers}

Consider ETA, Cost and Reliability.
"""

    response = ask_gpt(prompt)

    if response:

        decision = {
            "selected_carrier": "GPT-5 Recommendation",
            "reason": response,
        }

    else:

        best_score = -999
        best = None

        for carrier in carriers:

            score = (
                carrier["reliability"] * 2
                - carrier["eta_hours"]
                - carrier["cost"] / 1000
            )

            print("\n--------------------------------")
            print(f"Carrier      : {carrier['name']}")
            print(f"ETA          : {carrier['eta_hours']} Hours")
            print(f"Cost         : ₹{carrier['cost']}")
            print(f"Reliability  : {carrier['reliability']}%")
            print(f"Score        : {round(score,2)}")

            if score > best_score:
                best_score = score
                best = carrier

        decision = {
            "selected_carrier": best["name"],
            "eta": best["eta_hours"],
            "cost": best["cost"],
            "reliability": best["reliability"],
            "score": round(best_score, 2),
            "reason": "Highest overall evaluation score.",
        }

        print("\n✅ BEST CARRIER SELECTED")
        print(f"Carrier      : {best['name']}")
        print(f"ETA          : {best['eta_hours']} Hours")
        print(f"Cost         : ₹{best['cost']}")
        print(f"Reliability  : {best['reliability']}%")

    state["decision"] = decision
    return state


# -----------------------------
# Execution Agent
# -----------------------------
def execution_agent(state: WorkflowState):

    shipment = state["shipment"]
    decision = state["decision"]

    execution = {
        "shipment_id": shipment["shipment_id"],
        "new_carrier": decision["selected_carrier"],
        "status": "Shipment Successfully Rerouted",
        "notification": f"Shipment {shipment['shipment_id']} rerouted successfully.",
    }

    print("\n" + "=" * 60)
    print("⚙️ EXECUTION AGENT")
    print("=" * 60)

    print(f"Previous Carrier : {shipment['current_carrier']}")
    print(f"New Carrier      : {decision['selected_carrier']}")
    print(f"Status           : {execution['status']}")
    print("Notification     : Sent Successfully")

    state["execution"] = execution

    return state