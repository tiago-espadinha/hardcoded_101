import hashlib
from bisect import bisect_right
from typing import List, Optional


class ConsistentHashRing:
    """
    Implements consistent hashing with virtual nodes to ensure balanced distribution.
    
    Attributes:
        virtual_nodes (int): The number of virtual nodes per physical node.
        ring (List[int]): A sorted list of hashes representing the ring.
        nodes (dict): A mapping from hash to physical node.
    """

    def __init__(self, virtual_nodes: int = 150):
        self.virtual_nodes = virtual_nodes
        self.ring: List[int] = []
        self.nodes: dict[int, str] = {}

    def _hash(self, key: str) -> int:
        """Generates an integer hash for a given key."""
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def add_node(self, node: str) -> None:
        """Adds a physical node to the ring by creating virtual nodes."""
        for i in range(self.virtual_nodes):
            # Create a unique key for each virtual node
            v_node_key = f"{node}:{i}"
            h = self._hash(v_node_key)
            self.ring.append(h)
            self.nodes[h] = node
        
        self.ring.sort()

    def remove_node(self, node: str) -> None:
        """Removes a physical node and its virtual nodes from the ring."""
        for i in range(self.virtual_nodes):
            v_node_key = f"{node}:{i}"
            h = self._hash(v_node_key)
            if h in self.nodes:
                self.ring.remove(h)
                del self.nodes[h]

    def get_node(self, key: str) -> Optional[str]:
        """Returns the physical node responsible for the given key."""
        if not self.ring:
            return None

        h = self._hash(key)
        # Find the first virtual node hash greater than or equal to the key's hash
        idx = bisect_right(self.ring, h)
        
        # If we reach the end of the ring, wrap around to the first node
        if idx == len(self.ring):
            idx = 0
            
        return self.nodes[self.ring[idx]]
