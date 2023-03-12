import json
import logging
from .config import AppConfig
from .parser import ParserFactory

# Notification Facade
class NotificationFacade:
    def __init__(self):
        self.config = AppConfig().data

    def notify(self, message: str):
        print(f"Connecting to SMTP server {self.config['smtp_server']}...")
        print(f"Authenticating as {self.config['smtp_user']}...")
        print(f"Sending email: {message}")
        print("Closing connection.")

# Main Processor (Simplified)
class DataProcessor:
    def __init__(self):
        self.logger = logging.getLogger("DataProcessor")
        self.notifier = NotificationFacade()

    def process(self, source_type: str, file_path: str):
        self.logger.info(f"Processing {source_type} from {file_path}")
        
        # Use Factory
        parser = ParserFactory.get_parser(source_type)
        data = parser.parse(file_path)
        
        # Formatting (could be a Strategy, kept simple for brevity)
        formatted = self._format(data)
        
        # Saving
        output_file = f"processed_{file_path.split('.')[0]}.json"
        with open(output_file, 'w') as f:
            json.dump(formatted, f)
            
        # Use Facade
        self.notifier.notify(f"Success processing {file_path}")

    def _format(self, data):
        return [{
            "display_name": item["name"].upper(),
            "scaled_value": float(item["value"]) * 1.5,
            "status": "processed"
        } for item in data if "name" in item]
