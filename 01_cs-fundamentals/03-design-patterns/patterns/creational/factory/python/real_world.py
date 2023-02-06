from typing import Any, Dict
from pattern import ParserFactory

def process_document(file_name: str, raw_data: str) -> None:
    """Uses a Factory to get the right parser for the file extension."""
    extension = file_name.split('.')[-1]
    
    try:
        parser = ParserFactory.create_parser(extension)
        result = parser.parse(raw_data)
        print(f"Processed {file_name} with result: {result}")
    except ValueError as e:
        print(f"Error processing {file_name}: {e}")

if __name__ == "__main__":
    json_data = '{"name": "Alice", "role": "Dev"}'
    csv_data = 'name,role\nBob,Designer\nCharlie,Manager'
    
    process_document("data.json", json_data)
    process_document("report.csv", csv_data)
    process_document("manual.pdf", "PDF data...")
    process_document("unsupported.txt", "Text...")
