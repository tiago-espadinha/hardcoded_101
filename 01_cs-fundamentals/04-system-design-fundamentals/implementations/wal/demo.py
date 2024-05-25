import os
from wal import WAL

def simulate_kv_store(ops):
    store = {}
    for op in ops:
        if op['type'] == 'set':
            store[op['key']] = op['value']
        elif op['type'] == 'delete':
            store.pop(op['key'], None)
    return store

if __name__ == "__main__":
    log_file = "test.log"
    if os.path.exists(log_file): os.remove(log_file)
    
    wal = WAL(log_file)
    
    # Normal operations
    wal.append({'type': 'set', 'key': 'a', 'value': 1})
    wal.append({'type': 'set', 'key': 'b', 'value': 2})
    
    print("Initial Recovery:", simulate_kv_store(wal.recover()))
    
    # Simulate a crash during a write
    with open(log_file, 'a') as f:
        f.write('{"type": "set", "key": "c", "value": 3') # Partial write (no closing brace)
        
    print("Recovery after partial write:", simulate_kv_store(wal.recover()))
    
    # Add a successful write after recovery
    wal.append({'type': 'set', 'key': 'd', 'value': 4})
    print("Final Recovery:", simulate_kv_store(wal.recover()))
    
    if os.path.exists(log_file): os.remove(log_file)
