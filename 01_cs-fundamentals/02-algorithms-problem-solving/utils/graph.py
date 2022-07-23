from typing import Dict, List, Any, Optional

class Graph:
    """Graph implementation using an adjacency list."""
    def __init__(self, directed: bool = False):
        self.adj: Dict[Any, List[Any]] = {}
        self.weights: Dict[tuple[Any, Any], float] = {}
        self.directed = directed

    def add_node(self, node: Any) -> None:
        """Adds a node to the graph if it doesn't already exist."""
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, u: Any, v: Any, weight: Optional[float] = None) -> None:
        """Adds an edge between nodes u and v with an optional weight."""
        self.add_node(u)
        self.add_node(v)
        if v not in self.adj[u]:
            self.adj[u].append(v)
        if not self.directed:
            if u not in self.adj[v]:
                self.adj[v].append(u)
        
        if weight is not None:
            self.weights[(u, v)] = weight
            if not self.directed:
                self.weights[(v, u)] = weight

    def __str__(self) -> str:
        res = []
        for node, neighbors in self.adj.items():
            res.append(f"{node}: {', '.join(map(str, neighbors))}")
        return "\n".join(res)
