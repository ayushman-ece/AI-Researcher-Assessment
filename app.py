from config import Config
from workflow import build_workflow


def print_banner():
    print("=" * 60)
    print("AI Researcher Assessment")
    print("Autonomous Logistics Rerouting using LangGraph")
    print("=" * 60)


def main():

    print_banner()

    workflow = build_workflow()

    initial_state = {
        "shipment": Config.DEFAULT_SHIPMENT,
        "telemetry": {},
        "decision": {},
        "execution": {},
    }

    print("\nIncoming Shipment Alert")
    print("-" * 60)

    for key, value in Config.DEFAULT_SHIPMENT.items():
        print(f"{key:25}: {value}")

    print("\nRunning AI Multi-Agent Workflow...\n")

    result = workflow.invoke(initial_state)

    shipment = result["shipment"]
    telemetry = result["telemetry"]
    decision = result["decision"]
    execution = result["execution"]

    print("\n" + "=" * 60)
    print("📋 FINAL WORKFLOW SUMMARY")
    print("=" * 60)

    print(f"\nShipment ID      : {shipment['shipment_id']}")
    print(f"Origin           : {shipment['origin']}")
    print(f"Destination      : {shipment['destination']}")

    print("\nShipment Status")
    print("-" * 60)
    print(f"Current Carrier  : {shipment['current_carrier']}")
    print(f"Selected Carrier : {decision['selected_carrier']}")

    print("\nDelay Information")
    print("-" * 60)
    print(f"Reason           : {telemetry['delay_reason']}")
    print(f"Delay            : {telemetry['delay_hours']} Hours")
    print(f"Severity         : {telemetry['severity']}")

    print("\nDecision Summary")
    print("-" * 60)

    if "eta" in decision:
        print(f"Estimated ETA    : {decision['eta']} Hours")

    if "cost" in decision:
        print(f"Estimated Cost   : ₹{decision['cost']}")

    if "reliability" in decision:
        print(f"Reliability      : {decision['reliability']}%")

    if "score" in decision:
        print(f"Decision Score   : {decision['score']}")

    print(f"Reason           : {decision['reason']}")

    print("\nExecution")
    print("-" * 60)
    print(f"Status           : {execution['status']}")
    print(f"Notification     : {execution['notification']}")

    print("\n" + "=" * 60)
    print("✅ AI MULTI-AGENT WORKFLOW EXECUTED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()