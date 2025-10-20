from typing import Dict, List
import json, os
from adk_shim import tool

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "calendar.json")

@tool(name="get_free_slots", description="List 30-min slots for a given YYYY-MM-DD.")
def get_free_slots(date: str) -> Dict[str, List[str]]:
    cal = {}
    if os.path.exists(DATA):
        with open(DATA, "r") as f:
            cal = json.load(f)
    return {"date": date, "slots": cal.get(date, [])}
