"""
Fractional Knapsack: A Greedy approach to solving the knapsack problem.

This problem is different from the 0/1 Knapsack (which requires DP) in that 
we can take fractions of items. This allows for a much simpler Greedy solution.
"""
from typing import List, Tuple

def fractional_knapsack(items: List[Tuple[int, int]], capacity: int) -> Tuple[float, List[Tuple[int, float]]]:
    """
    Solves the Fractional Knapsack problem using a Greedy approach.
    
    The strategy is to sort items by their value-to-weight ratio and then add them 
    to the knapsack until it's full.
    
    Args:
        items: A list of tuples, where each tuple is (value, weight).
        capacity: The maximum capacity of the knapsack.
        
    Returns:
        A tuple containing:
        - The maximum total value.
        - The list of items (or fractions of items) included in the knapsack, 
          represented as (original_weight, fraction_taken).
          
    Complexity:
        Time: O(n log n) - due to sorting the items by value/weight ratio.
        Space: O(n) - to store the sorted items and the result.
    """
    if not items or capacity <= 0:
        return 0.0, []

    # Calculate value-to-weight ratio and store with original item data
    # item format: (value, weight, ratio)
    items_with_ratio = [(v, w, v / w) for v, w in items if w > 0]
    
    # Sort items by their value-to-weight ratio in descending order
    items_with_ratio.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0.0
    knapsack = []
    
    for value, weight, ratio in items_with_ratio:
        if capacity == 0:
            break
            
        # If the item fits completely, take it all
        if weight <= capacity:
            total_value += value
            knapsack.append((weight, 1.0)) # (weight, fraction)
            capacity -= weight
        else:
            # If the item doesn't fit, take a fraction of it
            fraction = capacity / weight
            total_value += value * fraction
            knapsack.append((weight, fraction))
            capacity = 0 # Knapsack is now full
            
    return total_value, knapsack

if __name__ == "__main__":
    # Example: (value, weight)
    example_items = [(60, 10), (100, 20), (120, 30)]
    knapsack_capacity = 50
    
    max_value, selected_items = fractional_knapsack(example_items, knapsack_capacity)
    
    print(f"Knapsack Capacity: {knapsack_capacity}")
    print("
Available items (value, weight):")
    for v, w in example_items:
        print(f"  Value: {v}, Weight: {w}")

    print(f"
Maximum value in knapsack: {max_value:.2f}")
    
    print("
Items in knapsack (original_weight, fraction_taken):")
    for weight, fraction in selected_items:
        print(f"  Weight: {weight}, Fraction: {fraction:.2f}")
        
    # Another detailed example
    print("
" + "="*20 + "
")
    
    more_items = [(10, 2), (5, 3), (15, 5), (7, 7), (6, 1), (18, 4), (3, 1)]
    capacity = 15
    
    max_val, in_knapsack = fractional_knapsack(more_items, capacity)

    print(f"Knapsack capacity: {capacity}")
    print("Available items (value, weight):", more_items)
    print(f"Maximum value: {max_val:.2f}")
    
    print("Fractions of items taken:")
    total_weight_in_knapsack = 0
    for i, (orig_w, frac) in enumerate(in_knapsack):
        item_val = 0
        for v, w in more_items:
            # This is inefficient, but just for demonstration
            if w == orig_w:
                item_val = v
                break
        
        print(f"  Item (Value: {item_val}, Weight: {orig_w}): took {frac * 100:.2f}%")
        total_weight_in_knapsack += orig_w * frac
    
    print(f"Total weight in knapsack: {total_weight_in_knapsack:.2f}")

