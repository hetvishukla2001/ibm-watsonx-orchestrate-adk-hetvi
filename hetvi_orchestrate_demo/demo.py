# Local console runner to "chat" with the agent via tool calls.
# Mirrors Orchestrate's idea: route user intents to tools.

import importlib, pkgutil, os, sys
from adk_shim import registry

# Ensure we can import tools as a package even when run directly
THIS_DIR = os.path.dirname(__file__)
TOOLS_DIR = os.path.join(THIS_DIR, "tools")
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

# Auto-import all modules in tools/ so @tool decorators register themselves
for _, module_name, _ in pkgutil.iter_modules([TOOLS_DIR]):
    importlib.import_module(module_name)

HELP = """
Commands:
  free <YYYY-MM-DD>                 # list slots
  propose <YYYY-MM-DD> <HH:MM>      # draft email text
  record <name> <YYYY-MM-DD> <HH:MM># log decision to data/decisions.csv
  help                              # show this
  exit                              # quit
"""

def main():
    print("=== Interview Scheduler Agent (Local, Orchestrate-style) ===")
    print(HELP)
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nbye!")
            break
        if not line:
            continue
        if line in ("exit", "quit"):
            print("bye!")
            break
        if line == "help":
            print(HELP)
            continue

        parts = line.split()
        cmd = parts[0].lower()

        try:
            if cmd == "free" and len(parts) == 2:
                print(registry.call("get_free_slots", parts[1]))
            elif cmd == "propose" and len(parts) == 3:
                print("\n" + registry.call("draft_proposal", parts[1], parts[2]) + "\n")
            elif cmd == "record" and len(parts) == 4:
                print(registry.call("record_choice", parts[1], parts[2], parts[3]))
            else:
                print("Unrecognized command or wrong args. Type 'help'.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
