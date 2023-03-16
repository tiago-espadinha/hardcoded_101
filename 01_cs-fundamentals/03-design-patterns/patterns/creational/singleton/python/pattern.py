import threading
from typing import Any, Dict

class ConfigManager:
    """
    A thread-safe Singleton configuration manager.
    Uses __new__ to ensure only one instance is created.
    """
    _instance = None
    _lock = threading.Lock()
    _settings: Dict[str, Any] = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def set(self, key: str, value: Any) -> None:
        """Sets a configuration setting."""
        with self._lock:
            self._settings[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Gets a configuration setting."""
        with self._lock:
            return self._settings.get(key, default)

if __name__ == "__main__":
    config1 = ConfigManager()
    config2 = ConfigManager()
    
    print(f"config1 is config2: {config1 is config2}")
    
    config1.set("app_name", "DesignPatternsDemo")
    print(f"App Name (from config2): {config2.get('app_name')}")
