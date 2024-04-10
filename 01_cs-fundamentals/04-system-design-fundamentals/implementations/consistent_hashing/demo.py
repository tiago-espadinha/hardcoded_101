import statistics
from consistent_hash import ConsistentHashRing

def print_distribution(counts: dict[str, int]) -> None:
    """Helper function to print distribution and its standard deviation."""
    print("--- Current Key Distribution ---")
    for node, count in sorted(counts.items()):
        print(f"Node {node}: {count} keys")
    
    # Calculate standard deviation to measure balance
    std_dev = statistics.stdev(counts.values()) if len(counts) > 1 else 0
    print(f"Standard Deviation: {std_dev:.2f}")
    print("--------------------------------\n")

def main():
    # 1. Initialize the ring and add 5 nodes
    # Default 150 virtual nodes per physical node
    ring = ConsistentHashRing(virtual_nodes=150)
    initial_nodes = [f"node-{i}" for i in range(1, 6)]
    for node in initial_nodes:
        ring.add_node(node)
    
    print(f"Added nodes: {initial_nodes}\n")

    # 2. Hash 10,000 keys
    num_keys = 10_000
    keys = [f"user_{i}" for i in range(num_keys)]
    
    # Store initial mapping to track redistribution
    initial_mapping = {}
    distribution = {node: 0 for node in initial_nodes}
    for key in keys:
        node = ring.get_node(key)
        initial_mapping[key] = node
        distribution[node] += 1
    
    print_distribution(distribution)

    # 3. Remove a node and show redistribution
    node_to_remove = "node-3"
    print(f"Removing {node_to_remove}...")
    ring.remove_node(node_to_remove)
    
    # Re-calculate distribution and track reassigned keys
    reassigned_count = 0
    new_distribution = {node: 0 for node in initial_nodes if node != node_to_remove}
    for key in keys:
        new_node = ring.get_node(key)
        new_distribution[new_node] += 1
        if new_node != initial_mapping[key]:
            reassigned_count += 1

    print(f"Keys reassigned after removal: {reassigned_count} (Expected: ~{distribution[node_to_remove]})")
    print_distribution(new_distribution)

    # 4. Add a new node and show redistribution
    new_node = "node-6"
    print(f"Adding {new_node}...")
    ring.add_node(new_node)
    
    final_nodes = [node for node in initial_nodes if node != node_to_remove] + [new_node]
    final_distribution = {node: 0 for node in final_nodes}
    reassigned_after_add = 0
    for key in keys:
        current_node = ring.get_node(key)
        final_distribution[current_node] += 1
        # Check if it's different from the state AFTER removal
        # (Though usually compared to INITIAL state)
        if current_node == new_node:
            reassigned_after_add += 1

    print(f"Keys reassigned after adding {new_node}: {reassigned_after_add}")
    print_distribution(final_distribution)

if __name__ == "__main__":
    main()
