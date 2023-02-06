from abc import ABC, abstractmethod
from typing import Dict, Any

class DocumentParser(ABC):
    """Abstract Base Class for parsers."""
    @abstractmethod
    def parse(self, data: str) -> Dict[str, Any]:
        pass

class JSONParser(DocumentParser):
    def parse(self, data: str) -> Dict[str, Any]:
        import json
        return json.loads(data)

class CSVParser(DocumentParser):
    def parse(self, data: str) -> Dict[str, Any]:
        # Minimal mock CSV parsing logic
        rows = [line.split(',') for line in data.strip().split('\n')]
        headers = rows[0]
        return {"type": "CSV", "data": [dict(zip(headers, row)) for row in rows[1:]]}

class PDFParser(DocumentParser):
    def parse(self, data: str) -> Dict[str, Any]:
        return {"type": "PDF", "content": "Parsed PDF content (Mock)"}

class ParserFactory:
    """Factory Method to create document parsers."""
    _parsers = {
        'json': JSONParser,
        'csv': CSVParser,
        'pdf': PDFParser
    }

    @staticmethod
    def create_parser(file_type: str) -> DocumentParser:
        parser_cls = ParserFactory._parsers.get(file_type.lower())
        if not parser_cls:
            raise ValueError(f"No parser available for type: {file_type}")
        return parser_cls()

if __name__ == "__main__":
    factory = ParserFactory()
    
    json_parser = factory.create_parser("json")
    print(f"JSON Output: {json_parser.parse('{\"key\": \"value\"}')}")
    
    csv_parser = factory.create_parser("csv")
    print(f"CSV Output: {csv_parser.parse('id,name\\n1,Alice')}")
