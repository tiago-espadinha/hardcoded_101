from abc import ABC, abstractmethod

class DataPipeline(ABC):
    """Abstract base class for a data pipeline (ETL)."""
    
    def run(self):
        """The template method defines the skeleton of the algorithm."""
        print(f"\n--- Starting Data Pipeline: {self.__class__.__name__} ---")
        data = self.extract()
        transformed_data = self.transform(data)
        self.load(transformed_data)
        print("--- Pipeline Finished ---")

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    @abstractmethod
    def load(self, data):
        pass

class CSVPipeline(DataPipeline):
    def extract(self):
        print("Extracting data from CSV file...")
        return "csv_raw_data"

    def transform(self, data):
        print(f"Transforming {data} to structured format...")
        return {"source": "csv", "content": data.upper()}

    def load(self, data):
        print(f"Loading {data} into Data Warehouse...")

class DBPipeline(DataPipeline):
    def extract(self):
        print("Extracting data from SQL Database...")
        return "db_raw_data"

    def transform(self, data):
        print(f"Transforming {data} using complex SQL logic...")
        return {"source": "sql", "content": data.replace("_", " ")}

    def load(self, data):
        print(f"Loading {data} into Analytics Dashboard...")

if __name__ == "__main__":
    csv_pipeline = CSVPipeline()
    csv_pipeline.run()
    
    db_pipeline = DBPipeline()
    db_pipeline.run()
