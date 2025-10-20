from adk_shim import tool

@tool(name="draft_proposal", description="Draft an email snippet proposing a slot to a person.")
def draft_proposal(name: str, date: str, time: str) -> str:
    """Draft a polite email suggesting a meeting time."""
    return (
        f"Hi {name},\n\n"
        f"Does {date} at {time} (30 minutes) work for you? "
        f"If not, I can share a couple of alternatives.\n\nThanks,\nHetvi"
    )
