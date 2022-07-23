from collections import deque
from typing import Dict, List, Set, Optional

def bfs(graph: Dict[int, List[int]], start_node: int) -> List[int]:
    """
    Performs a Breadth-First Search (BFS) on an adjacency list.
    Time complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Space complexity: O(V) for the queue and the visited set.
    
    Args:
        graph: The graph represented as an adjacency list.
        start_node: The node where the search begins.
        
    Returns:
        The list of nodes visited in BFS order.
    """
    visited: Set[int] = {start_node}
    queue = deque([start_node])
    traversal_order: List[int] = []
    
    while queue:
        node = queue.popleft()
        traversal_order.append(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_order

if __name__ == "__main__":
    # Graph representation (Adjacency List)
    #    0 -- 1 -- 3
    #    |    |    |
    #    2 ---'    4
    graph = {
        0: [1, 2],
        1: [0, 3, 2],
        2: [0, 1],
        3: [1, 4],
        4: [3]
    }
    
    print(f"Graph: {graph}")
    print(f"BFS starting from 0: {bfs(graph, 0)}")
    print(f"BFS starting from 3: {bfs(graph, 3)}")
