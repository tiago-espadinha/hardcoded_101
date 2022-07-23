"""
Huffman Coding: A Greedy algorithm for lossless data compression.

This module provides functions to build a Huffman Tree from a given text and 
then use it to encode and decode the text.
"""
import heapq
from collections import defaultdict, Counter

class Node:
    """A node in the Huffman Tree."""
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        """Less-than comparison for heapq."""
        return self.freq < other.freq

def build_huffman_tree(text: str):
    """
    Builds a Huffman Tree from the given text.
    
    The tree is constructed by assigning shorter codes to more frequent characters 
    and longer codes to less frequent ones.
    
    - Time complexity: O(n log n) where n is the number of unique characters.
    - Space complexity: O(n) for storing the frequency map and the tree.
    """
    if not text:
        return None, {}

    # Calculate frequency of each character
    freq = Counter(text)
    
    # Create a priority queue (min-heap) of nodes
    priority_queue = [Node(char, f) for char, f in freq.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        # Get the two nodes with the lowest frequency
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        # Create a new internal node with these two nodes as children
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Add the new node back to the priority queue
        heapq.heappush(priority_queue, merged)

    # The root of the Huffman Tree
    root = priority_queue[0]
    
    # Generate Huffman codes for each character
    codes = {}
    def generate_codes(node, prefix=""):
        if node is not None:
            if node.char is not None:
                codes[node.char] = prefix
            generate_codes(node.left, prefix + "0")
            generate_codes(node.right, prefix + "1")

    generate_codes(root)
    return root, codes

def encode(text: str, codes: dict) -> str:
    """Encodes the text using the given Huffman codes."""
    return "".join(codes[char] for char in text)

def decode(encoded_text: str, root) -> str:
    """Decodes the encoded text using the Huffman Tree."""
    if not root or not encoded_text:
        return ""

    decoded_text = []
    current_node = root
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text.append(current_node.char)
            current_node = root
            
    return "".join(decoded_text)

if __name__ == "__main__":
    text = "huffman coding is a lossless data compression algorithm"
    
    print(f"Original text: '{text}'")
    
    # Build the Huffman Tree and get the codes
    huffman_tree_root, huffman_codes = build_huffman_tree(text)
    
    print("
Huffman Codes:")
    for char, code in sorted(huffman_codes.items()):
        print(f"  '{char}': {code}")
        
    # Encode the text
    encoded_text = encode(text, huffman_codes)
    print(f"
Encoded text: {encoded_text}")

    # Decode the text
    decoded_text = decode(encoded_text, huffman_tree_root)
    print(f"Decoded text: '{decoded_text}'
")

    # Verify correctness
    assert text == decoded_text
    print("Successfully encoded and decoded the text!")
