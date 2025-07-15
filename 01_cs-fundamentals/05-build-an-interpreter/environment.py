from typing import Any, Dict, Optional

class Environment:
    def __init__(self, parent: Optional['Environment'] = None):
        self.values: Dict[str, Any] = {}
        self.parent = parent

    def define(self, name: str, value: Any):
        self.values[name] = value

    def get(self, name: str) -> Any:
        if name in self.values:
            return self.values[name]
        
        if self.parent:
            return self.parent.get(name)
        
        raise NameError(f"Undefined variable '{name}'.")

    def assign(self, name: str, value: Any):
        if name in self.values:
            self.values[name] = value
            return
        
        if self.parent:
            self.parent.assign(name, value)
            return
        
        raise NameError(f"Undefined variable '{name}'.")
