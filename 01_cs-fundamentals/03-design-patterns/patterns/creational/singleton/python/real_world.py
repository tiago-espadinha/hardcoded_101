import threading
import time
from typing import List, Optional

class DatabaseConnectionPool:
    """
    Real-world Singleton: A pool of database connections shared across the app.
    Ensures that multiple components use the same set of connections.
    """
    _instance: Optional['DatabaseConnectionPool'] = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize_pool()
        return cls._instance

    def _initialize_pool(self):
        self.pool: List[str] = ["Conn1", "Conn2", "Conn3", "Conn4", "Conn5"]
        self.busy_connections: List[str] = []
        print(f"Initialized Database Connection Pool with {len(self.pool)} connections.")

    def acquire_connection(self) -> str:
        with self._lock:
            if not self.pool:
                raise Exception("No connections available in the pool.")
            conn = self.pool.pop()
            self.busy_connections.append(conn)
            return conn

    def release_connection(self, conn: str) -> None:
        with self._lock:
            if conn in self.busy_connections:
                self.busy_connections.remove(conn)
                self.pool.append(conn)
            else:
                print(f"Warning: Connection {conn} was not from this pool.")

if __name__ == "__main__":
    # Simulate multi-threaded access
    pool1 = DatabaseConnectionPool()
    pool2 = DatabaseConnectionPool()
    
    print(f"pool1 is pool2: {pool1 is pool2}")
    
    conn = pool1.acquire_connection()
    print(f"Acquired: {conn}")
    pool2.release_connection(conn)
    print(f"Released: {conn} through pool2 reference")
