from pattern import CSVPipeline, DBPipeline

class LogIngestionService:
    """A service that handles different types of logs using specialized pipelines."""
    
    def __init__(self):
        self._pipelines = {
            "csv": CSVPipeline(),
            "db": DBPipeline()
        }
        
    def process_logs(self, log_type: str):
        pipeline = self._pipelines.get(log_type)
        if pipeline:
            pipeline.run()
        else:
            print(f"No pipeline found for log type: {log_type}")

if __name__ == "__main__":
    service = LogIngestionService()
    
    print("Processing nightly batch...")
    service.process_logs("csv")
    
    print("\nProcessing real-time stream...")
    service.process_logs("db")
