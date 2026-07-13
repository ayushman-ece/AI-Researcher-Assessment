from typing import TypedDict, Dict, Any

from langgraph.graph import StateGraph, END

from agents import (
    telemetry_agent,
    decision_agent,
    execution_agent,
)


class WorkflowState(TypedDict):
    shipment: Dict[str, Any]
    telemetry: Dict[str, Any]
    decision: Dict[str, Any]
    execution: Dict[str, Any]


def build_workflow():

    workflow = StateGraph(WorkflowState)

    # ----------------------------
    # Register Nodes
    # ----------------------------
    workflow.add_node("Telemetry", telemetry_agent)
    workflow.add_node("Decision", decision_agent)
    workflow.add_node("Execution", execution_agent)

    # ----------------------------
    # Flow
    # ----------------------------
    workflow.set_entry_point("Telemetry")

    workflow.add_edge("Telemetry", "Decision")
    workflow.add_edge("Decision", "Execution")
    workflow.add_edge("Execution", END)

    app = workflow.compile()

    return app