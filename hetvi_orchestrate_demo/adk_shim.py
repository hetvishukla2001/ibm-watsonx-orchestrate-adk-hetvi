# A tiny shim to mimic the Orchestrate ADK "tool" decorator and a registry.

from typing import Callable, Dict, Any, List

class ToolRegistry:
    def __init__(self) -> None:
        self.tools: Dict[str, Dict[str, Any]] = {}

    def register(self, fn: Callable, name: str, description: str) -> None:
        self.tools[name] = {"fn": fn, "description": description}

    def call(self, name: str, *args, **kwargs):
        return self.tools[name]["fn"](*args, **kwargs)

registry = ToolRegistry()

def tool(name: str, description: str):
    def decorator(fn: Callable):
        registry.register(fn, name=name, description=description)
        return fn
    return decorator
