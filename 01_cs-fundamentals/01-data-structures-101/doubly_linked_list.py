from typing import Any, Optional

class Node:
    def __init__(self, value: Any, prev_node: Optional['Node'] = None, next_node: Optional['Node'] = None):
        """
        Initialize a Node with value, prev, and next references.
        Args:
            value (Any): The data to store.
            prev_node (Node, optional): Reference to the previous node.
            next_node (Node, optional): Reference to the next node.
        """
        self.value = value
        self.prev = prev_node
        self.next = next_node

class DoublyLinkedList:
    def __init__(self):
        """
        Initialize an empty Doubly Linked List.
        """
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._length = 0

    # O(1)
    def prepend(self, value: Any) -> None:
        """
        Insert a new value at the beginning of the list.
        Args:
            value (Any): The value to prepend.
        Returns:
            None
        """
        new_node = Node(value, None, self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self._length += 1

    # O(1)
    def append(self, value: Any) -> None:
        """
        Insert a new value at the end of the list.
        Args:
            value (Any): The value to append.
        Returns:
            None
        """
        new_node = Node(value, self.tail, None)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self._length += 1

    # O(n)
    def delete(self, value: Any) -> bool:
        """
        Remove the first occurrence of a value from the list.
        Args:
            value (Any): The value to delete.
        Returns:
            bool: True if deleted, False otherwise.
        """
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self._length -= 1
                return True
            current = current.next
        return False

    # O(n)
    def search(self, value: Any) -> Optional[Node]:
        """
        Search for a value and return the corresponding Node.
        Args:
            value (Any): The value to find.
        Returns:
            Node|None: The node containing the value, or None if not found.
        """
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    # O(n)
    def to_list(self) -> list[Any]:
        """
        Convert the linked list to a standard Python list.
        Returns:
            list: A list containing all elements.
        """
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def __len__(self) -> int:
        """
        Return the number of elements in the list.
        Returns:
            int: The size of the list.
        """
        return self._length

    def __str__(self) -> str:
        """
        Return a string representation of the list.
        Returns:
            str: "None <- val1 <-> val2 -> None"
        """
        items = self.to_list()
        if not items:
            return "Empty"
        return "None <- " + " <-> ".join(map(str, items)) + " -> None"
