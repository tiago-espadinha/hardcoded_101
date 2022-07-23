import heapq
from typing import Dict, List, Tuple, Optional

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start_node: int) -> Dict[int, int]:
    """
    Computes the shortest distance from the start node to all other reachable nodes.
    Time complexity: O((V + E) log V) where V is vertices and E is edges.
    Space complexity: O(V) for distances and the priority queue.
    
    Args:
        graph: Adjacency list with weighted edges. Format: {node: [(neighbor, weight), ...]}
        start_node: Starting node for the algorithm.
        
    Returns:
        A dictionary mapping each reachable node to its shortest distance from start_node.
    """
    # Initialise distances with infinity
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    
    # Priority queue stores (distance, node)
    pq = [(0, start_node)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we found a longer path than already recorded, skip it
        if current_distance > distances.get(current_node, float('inf')):
            continue
            
        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight
            
            # If we found a shorter path to neighbor, update it
            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

if __name__ == "__main__":
    # Weighted graph representation (Adjacency List)
    #    0 --(4)-- 1 --(8)-- 3
    #    |        /|        /
    #   (1)    (2) (5)   (3)
    #    |    /    |    /
    #    2 --'     '-- 4
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 8), (2, 2), (4, 5)],
        2: [(1, 2)],
        3: [(4, 3)],
        4: [] # 4 has no outgoing edges
    }
    
    # Ensure nodes without outgoing edges are in the dictionary for initialisation
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        for n, w in neighbors:
            all_nodes.add(n)
    for n in all_nodes:
        if n not in graph:
            graph[n] = []
            
    print(f"Weighted Graph: {graph}")
    print(f"Dijkstra shortest paths from 0: {dijkstra(graph, 0)}")
    print(f"Dijkstra shortest paths from 2: {dijkstra(graph, 2)}")
