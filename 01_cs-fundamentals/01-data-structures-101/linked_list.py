from typing import Any, Optional

class Node:
    def __init__(self, value: Any, next_node: Optional['Node'] = None):
        """
        Initialize a Node with value and next reference.
        Args:
            value (Any): The data to store.
            next_node (Node, optional): Reference to the next node.
        """
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self):
        """
        Initialize an empty Singly Linked List.
        """
        self.head: Optional[Node] = None
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
        new_node = Node(value, self.head)
        self.head = new_node
        self._length += 1

    # O(n)
    def append(self, value: Any) -> None:
        """
        Insert a new value at the end of the list.
        Args:
            value (Any): The value to append.
        Returns:
            None
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
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
        if not self.head:
            return False

        if self.head.value == value:
            self.head = self.head.next
            self._length -= 1
            return True

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
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
    def reverse(self) -> None:
        """
        Reverse the order of elements in the linked list in-place.
        Returns:
            None
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

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
            str: "val1 -> val2 -> None"
        """
        items = self.to_list()
        return " -> ".join(map(str, items)) + " -> None" if items else "Empty"
