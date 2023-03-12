import json
import csv
import logging
from typing import List, Dict

# The "God Class"
class DataProcessor:
    """
    A 200-line "god class" doing too much (parsing, formatting, 
    saving, logging, sending emails all in one class).
    """
    def __init__(self, config_file: str):
        # Configuration management (Singleton candidate)
        self.config = self._load_config(config_file)
        # Logging setup (Decorator candidate)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("DataProcessor")

    def _load_config(self, path: str):
        with open(path, 'r') as f:
            return json.load(f)

    def process_data(self, source_type: str, file_path: str):
        self.logger.info(f"Starting process for {source_type} at {file_path}")
        
        # Parsing logic (Factory/Strategy candidate)
        data = []
        if source_type == "json":
            with open(file_path, 'r') as f:
                data = json.load(f)
        elif source_type == "csv":
            with open(file_path, 'r') as f:
                reader = csv.DictReader(f)
                data = list(reader)
        else:
            raise ValueError(f"Unsupported source type: {source_type}")

        # Formatting logic (Template Method/Strategy candidate)
        formatted_results = []
        for item in data:
            if "name" in item and "value" in item:
                formatted_results.append({
                    "display_name": item["name"].upper(),
                    "scaled_value": float(item["value"]) * 1.5,
                    "status": "processed"
                })

        # Saving logic (Command candidate)
        output_file = f"processed_{file_path.split('.')[0]}.json"
        with open(output_file, 'w') as f:
            json.dump(formatted_results, f)
        self.logger.info(f"Saved results to {output_file}")

        # Notification logic (Facade/Observer candidate)
        self._send_notification(f"Process complete for {file_path}")

    def _send_notification(self, message: str):
        # Complex notification subsystem (Facade candidate)
        print(f"Connecting to SMTP server {self.config['smtp_server']}...")
        print(f"Authenticating as {self.config['smtp_user']}...")
        print(f"Sending email: {message}")
        print("Closing connection.")

if __name__ == "__main__":
    # Create a dummy config file
    with open("config.json", "w") as f:
        json.dump({"smtp_server": "smtp.example.com", "smtp_user": "admin"}, f)
    
    # Create a dummy data file
    with open("data.json", "w") as f:
        json.dump([{"name": "test", "value": "10"}], f)

    processor = DataProcessor("config.json")
    processor.process_data("json", "data.json")
