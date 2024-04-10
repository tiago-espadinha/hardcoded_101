import numpy as np
from multiprocessing import Process, shared_memory
import time

def worker(shm_name, shape, dtype, start_idx, end_idx):
    # Connect to the existing shared memory
    existing_shm = shared_memory.SharedMemory(name=shm_name)
    # Create a numpy array backed by the shared memory
    arr = np.ndarray(shape, dtype=dtype, buffer=existing_shm.buf)
    
    # Fill the assigned slice
    print(f"Worker filling slice {start_idx}:{end_idx}")
    arr[start_idx:end_idx] = np.arange(start_idx, end_idx)
    
    # Close connection
    existing_shm.close()

def demo_shared_memory():
    # Array configuration
    shape = (1000000,)
    dtype = np.int64
    size = np.dtype(dtype).itemsize * np.prod(shape)
    
    # Create shared memory block
    shm = shared_memory.SharedMemory(create=True, size=size)
    try:
        # Create a numpy array backed by this shared memory
        main_arr = np.ndarray(shape, dtype=dtype, buffer=shm.buf)
        main_arr[:] = 0 # Initialize with zeros
        
        # Launch 4 processes to fill different parts
        processes = []
        n_procs = 4
        chunk_size = shape[0] // n_procs
        
        for i in range(n_procs):
            start = i * chunk_size
            end = (i + 1) * chunk_size if i < n_procs - 1 else shape[0]
            p = Process(target=worker, args=(shm.name, shape, dtype, start, end))
            processes.append(p)
            p.start()
            
        for p in processes:
            p.join()
            
        print("\nShared memory array populated.")
        print(f"First 10: {main_arr[:10]}")
        print(f"Last 10:  {main_arr[-10:]}")
        print(f"Sum:      {main_arr.sum()} (Expected {sum(range(shape[0]))})")
        
    finally:
        # Cleanup
        shm.close()
        shm.unlink()

if __name__ == "__main__":
    try:
        demo_shared_memory()
    except Exception as e:
        print(f"Error: {e}")
        print("Note: This script requires numpy.")
