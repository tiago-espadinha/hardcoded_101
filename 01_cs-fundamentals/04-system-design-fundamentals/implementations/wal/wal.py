import os
import json

class WAL:
    def __init__(self, log_path):
        self.log_path = log_path
        
    def append(self, op):
        with open(self.log_path, 'a') as f:
            f.write(json.dumps(op) + '\n')
            f.flush()
            os.fsync(f.fileno()) # Ensure it's on disk

    def recover(self):
        if not os.path.exists(self.log_path):
            return []
        ops = []
        with open(self.log_path, 'r') as f:
            for line in f:
                if line.strip():
                    try:
                        ops.append(json.loads(line))
                    except json.JSONDecodeError:
                        break # Partial write at the end
        return ops
