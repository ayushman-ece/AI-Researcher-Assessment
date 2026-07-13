import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Central configuration for the project.
    """

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    USE_MOCK = os.getenv("USE_MOCK", "true").lower() == "true"

    MODEL_NAME = "gpt-5"

    COMPANY_NAME = "Triluxo Pvt. Ltd."

    APP_NAME = "Autonomous Logistics Rerouting"

    DEFAULT_SHIPMENT = {
        "shipment_id": "SHIP-1001",
        "origin": "Delhi",
        "destination": "Mumbai",
        "current_carrier": "Carrier A",
        "delay_reason": "Heavy Rain",
        "expected_delay_hours": 6,
    }

    ALTERNATIVE_CARRIERS = [
        {
            "name": "Carrier B",
            "eta_hours": 18,
            "cost": 2200,
            "reliability": 92,
        },
        {
            "name": "Carrier C",
            "eta_hours": 20,
            "cost": 1800,
            "reliability": 87,
        },
        {
            "name": "Carrier D",
            "eta_hours": 17,
            "cost": 2600,
            "reliability": 95,
        },
    ]