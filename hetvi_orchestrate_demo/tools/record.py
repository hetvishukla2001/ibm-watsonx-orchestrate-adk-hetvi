import csv, os
from adk_shim import tool

LOG = os.path.join(os.path.dirname(__file__), "..", "data", "decisions.csv")
os.makedirs(os.path.dirname(LOG), exist_ok=True)

@tool(name="record_choice", description="Record the selected slot to a CSV log.")
def record_choice(candidate: str, date: str, time: str) -> str:
    write_header = not os.path.exists(LOG)
    with open(LOG, "a", newline="") as f:
        w = csv.writer(f)
        if write_header:
            w.writerow(["candidate", "date", "time"])
        w.writerow([candidate, date, time])
    return "Recorded."
