import json
import threading

class AppConfig:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(AppConfig, cls).__new__(cls)
                # Load some defaults
                cls._instance.data = {"smtp_server": "smtp.example.com", "smtp_user": "admin"}
        return cls._instance

    def load_from_file(self, path: str):
        with open(path, 'r') as f:
            self.data = json.load(f)
