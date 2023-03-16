import json
import csv
from abc import ABC, abstractmethod

class DataParser(ABC):
    @abstractmethod
    def parse(self, file_path: str):
        pass

class JSONParser(DataParser):
    def parse(self, file_path: str):
        with open(file_path, 'r') as f:
            return json.load(f)

class CSVParser(DataParser):
    def parse(self, file_path: str):
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            return list(reader)

class ParserFactory:
    @staticmethod
    def get_parser(source_type: str) -> DataParser:
        if source_type == "json":
            return JSONParser()
        elif source_type == "csv":
            return CSVParser()
        raise ValueError(f"Unknown source type: {source_type}")
