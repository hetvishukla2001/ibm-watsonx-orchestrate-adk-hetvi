import importlib, pkgutil, os, sys
from adk_shim import registry

THIS_DIR = os.path.dirname(__file__)
TOOLS_DIR = os.path.join(THIS_DIR, "tools")
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

for _, module_name, _ in pkgutil.iter_modules([TOOLS_DIR]):
    importlib.import_module(module_name)

HELP = """
Commands:
  free <YYYY-MM-DD>                         # List available time slots for that date
  propose <name> <YYYY-MM-DD> <HH:MM>       # Draft an email proposal to that person
  record <name> <YYYY-MM-DD> <HH:MM>        # Log a confirmed meeting to data/decisions.csv
  help                                      # Show this help message
  exit                                      # Quit the demo
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
            elif cmd == "propose" and len(parts) == 4:
                print("\n" + registry.call("draft_proposal", parts[1], parts[2], parts[3]) + "\n")

            elif cmd == "record" and len(parts) == 4:
                print(registry.call("record_choice", parts[1], parts[2], parts[3]))
            else:
                print("Unrecognized command or wrong args. Type 'help'.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
