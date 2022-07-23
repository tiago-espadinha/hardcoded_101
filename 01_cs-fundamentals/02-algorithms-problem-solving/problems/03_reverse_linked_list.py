"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list_brute_force(head: ListNode) -> ListNode:
    """
    Brute force: Using a stack or an array to store values.
    1. Traverse the linked list and store all node values in an array.
    2. Create a new linked list by creating new nodes from the reversed array.
    Time complexity: O(n) - We traverse the list twice (once to populate the array, once to build the new list).
    Space complexity: O(n) - To store the node values in the array.
    """
    if not head:
        return None

    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next

    dummy = new_head = ListNode(vals.pop())
    while vals:
        new_head.next = ListNode(vals.pop())
        new_head = new_head.next

    return dummy

def reverse_list_optimized(head: ListNode) -> ListNode:
    """
    Optimized: Iterative solution with three pointers.
    We iterate through the list, changing the `next` pointer of each node to point to its predecessor.
    Time complexity: O(n) - We traverse the list once.
    Space complexity: O(1) - We only use a few pointers.
    """
    prev = None
    curr = head
    while curr:
        next_temp = curr.next  # Store the next node
        curr.next = prev       # Reverse the current node's pointer
        prev = curr            # Move pointers one position ahead
        curr = next_temp
    return prev

# Helper function to create a linked list from a list
def create_linked_list(items):
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    items = []
    current = head
    while current:
        items.append(current.val)
        current = current.next
    return items

# Test cases
# Brute Force
list1 = create_linked_list([1, 2, 3, 4, 5])
reversed_list1 = reverse_list_brute_force(list1)
assert linked_list_to_list(reversed_list1) == [5, 4, 3, 2, 1]

list2 = create_linked_list([1, 2])
reversed_list2 = reverse_list_brute_force(list2)
assert linked_list_to_list(reversed_list2) == [2, 1]

list3 = create_linked_list([])
reversed_list3 = reverse_list_brute_force(list3)
assert linked_list_to_list(reversed_list3) == []

# Optimized
list4 = create_linked_list([1, 2, 3, 4, 5])
reversed_list4 = reverse_list_optimized(list4)
assert linked_list_to_list(reversed_list4) == [5, 4, 3, 2, 1]

list5 = create_linked_list([1, 2])
reversed_list5 = reverse_list_optimized(list5)
assert linked_list_to_list(reversed_list5) == [2, 1]

list6 = create_linked_list([])
reversed_list6 = reverse_list_optimized(list6)
assert linked_list_to_list(reversed_list6) == []
