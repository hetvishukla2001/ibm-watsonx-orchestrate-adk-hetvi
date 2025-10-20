from adk_shim import tool

@tool(name="draft_proposal", description="Draft an email snippet proposing a slot.")
def draft_proposal(date: str, time: str) -> str:
    return (
        f"Hi Alessandro,\n\n"
        f"Does {date} at {time} (30 minutes) work for you? "
        f"If not, I can share a couple of alternatives.\n\nThanks,\nHetvi"
    )
