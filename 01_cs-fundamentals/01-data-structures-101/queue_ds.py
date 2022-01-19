from typing import Any, Optional
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        """
        Initialize an empty Queue backed by a Doubly Linked List.
        """
        self._items = DoublyLinkedList()

    # O(1)
    def enqueue(self, value: Any) -> None:
        """
        Add an item to the end of the queue.
        Args:
            value (Any): The value to enqueue.
        Returns:
            None
        """
        self._items.append(value)

    # O(1)
    def dequeue(self) -> Any:
        """
        Remove and return the front item of the queue.
        Returns:
            Any: The dequeued value.
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        
        value = self._items.head.value
        self._items.delete(value)
        return value

    # O(1)
    def peek(self) -> Any:
        """
        Return the front item of the queue without removing it.
        Returns:
            Any: The front value.
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items.head.value

    # O(1)
    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        Returns:
            bool: True if empty, False otherwise.
        """
        return len(self._items) == 0

    # O(1)
    def size(self) -> int:
        """
        Return the number of items in the queue.
        Returns:
            int: The size of the queue.
        """
        return len(self._items)

    def __str__(self) -> str:
        """
        Return a string representation of the queue.
        Returns:
            str: "Queue: front -> val1 <-> val2 -> back"
        """
        items = self._items.to_list()
        if not items:
            return "Queue: Empty"
        return "Queue: " + " <-> ".join(map(str, items))
