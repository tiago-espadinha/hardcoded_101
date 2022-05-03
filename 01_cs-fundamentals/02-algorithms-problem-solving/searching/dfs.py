from typing import Dict, List, Set, Optional

def dfs_recursive(graph: Dict[int, List[int]], start_node: int, visited: Optional[Set[int]] = None) -> List[int]:
    """
    Performs a recursive Depth-First Search (DFS) on an adjacency list.
    Time complexity: O(V + E) where V is vertices and E is edges.
    Space complexity: O(V) for the visited set and recursion stack.
    
    Args:
        graph: Adjacency list representation of the graph.
        start_node: Starting node for the search.
        visited: Set of nodes already visited.
        
    Returns:
        The list of nodes visited in DFS order.
    """
    if visited is None:
        visited = set()
    
    visited.add(start_node)
    traversal_order = [start_node]
    
    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            traversal_order.extend(dfs_recursive(graph, neighbor, visited))
            
    return traversal_order

def dfs_iterative(graph: Dict[int, List[int]], start_node: int) -> List[int]:
    """
    Performs an iterative Depth-First Search (DFS) on an adjacency list.
    Time complexity: O(V + E)
    Space complexity: O(V)
    
    Args:
        graph: Adjacency list representation of the graph.
        start_node: Starting node for the search.
        
    Returns:
        The list of nodes visited in DFS order.
    """
    visited: Set[int] = set()
    stack = [start_node]
    traversal_order: List[int] = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            # Reversing neighbor order to match recursive behavior
            # when adding to stack, but it's not strictly required
            # as long as we visit all neighbors.
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
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
    print(f"Recursive DFS starting from 0: {dfs_recursive(graph, 0)}")
    print(f"Iterative DFS starting from 0: {dfs_iterative(graph, 0)}")
    print(f"\nDFS starting from 3:")
    print(f"Recursive: {dfs_recursive(graph, 3)}")
    print(f"Iterative: {dfs_iterative(graph, 3)}")
