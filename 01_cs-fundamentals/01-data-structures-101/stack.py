from typing import Any, Optional
from linked_list import LinkedList

class Stack:
    def __init__(self):
        """
        Initialize an empty Stack backed by a Singly Linked List.
        """
        self._items = LinkedList()

    # O(1)
    def push(self, value: Any) -> None:
        """
        Add an item to the top of the stack.
        Args:
            value (Any): The value to push.
        Returns:
            None
        """
        self._items.prepend(value)

    # O(1)
    def pop(self) -> Any:
        """
        Remove and return the top item of the stack.
        Returns:
            Any: The popped value.
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        
        value = self._items.head.value
        self._items.delete(value)
        return value

    # O(1)
    def peek(self) -> Any:
        """
        Return the top item of the stack without removing it.
        Returns:
            Any: The top value.
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items.head.value

    # O(1)
    def is_empty(self) -> bool:
        """
        Check if the stack is empty.
        Returns:
            bool: True if empty, False otherwise.
        """
        return len(self._items) == 0

    # O(1)
    def size(self) -> int:
        """
        Return the number of items in the stack.
        Returns:
            int: The size of the stack.
        """
        return len(self._items)

    def __str__(self) -> str:
        """
        Return a string representation of the stack.
        Returns:
            str: "Stack: top -> val1 -> val2 -> None"
        """
        return f"Stack: {str(self._items)}"
