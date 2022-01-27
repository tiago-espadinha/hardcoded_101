from typing import Any, Optional, List

class Node:
    def __init__(self, value: Any, left: Optional['Node'] = None, right: Optional['Node'] = None):
        """
        Initialize a BST Node.
        Args:
            value (Any): The data to store.
            left (Node, optional): Left child.
            right (Node, optional): Right child.
        """
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        """
        Initialize an empty Binary Search Tree.
        """
        self.root: Optional[Node] = None

    # O(log n) avg, O(n) worst
    def insert(self, value: Any) -> None:
        """
        Insert a value into the BST.
        Args:
            value (Any): The value to insert.
        Returns:
            None
        """
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current: Node, value: Any) -> None:
        if value < current.value:
            if current.left:
                self._insert_recursive(current.left, value)
            else:
                current.left = Node(value)
        elif value > current.value:
            if current.right:
                self._insert_recursive(current.right, value)
            else:
                current.right = Node(value)
        # Duplicate values are ignored by default

    # O(log n) avg, O(n) worst
    def search(self, value: Any) -> bool:
        """
        Search for a value in the BST.
        Args:
            value (Any): The value to find.
        Returns:
            bool: True if found, False otherwise.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current: Optional[Node], value: Any) -> bool:
        if not current:
            return False
        if current.value == value:
            return True
        if value < current.value:
            return self._search_recursive(current.left, value)
        return self._search_recursive(current.right, value)

    # O(log n) avg, O(n) worst
    def delete(self, value: Any) -> None:
        """
        Delete a value from the BST.
        Args:
            value (Any): The value to delete.
        Returns:
            None
        """
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current: Optional[Node], value: Any) -> Optional[Node]:
        if not current:
            return None

        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            # Node to delete found
            if not current.left:
                return current.right
            elif not current.right:
                return current.left
            
            # Node with two children: Get inorder successor
            min_larger_node = self._min_node(current.right)
            current.value = min_larger_node.value
            current.right = self._delete_recursive(current.right, min_larger_node.value)
        
        return current

    def _min_node(self, node: Node) -> Node:
        current = node
        while current.left:
            current = current.left
        return current

    # O(n)
    def inorder(self) -> List[Any]:
        """
        Return list of values in inorder traversal.
        Returns:
            List[Any]: Values in order.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[Node], result: List[Any]):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    # O(n)
    def preorder(self) -> List[Any]:
        """
        Return list of values in preorder traversal.
        Returns:
            List[Any]: Values in preorder.
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node: Optional[Node], result: List[Any]):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    # O(n)
    def postorder(self) -> List[Any]:
        """
        Return list of values in postorder traversal.
        Returns:
            List[Any]: Values in postorder.
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node: Optional[Node], result: List[Any]):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    # O(n)
    def height(self) -> int:
        """
        Return the height of the BST.
        Returns:
            int: The height (max depth).
        """
        return self._height_recursive(self.root)

    def _height_recursive(self, node: Optional[Node]) -> int:
        if not node:
            return 0
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))

    # O(log n) avg, O(n) worst
    def min_value(self) -> Any:
        """
        Return the minimum value in the BST.
        Returns:
            Any: The minimum value.
        """
        if not self.root:
            return None
        return self._min_node(self.root).value

    # O(log n) avg, O(n) worst
    def max_value(self) -> Any:
        """
        Return the maximum value in the BST.
        Returns:
            Any: The maximum value.
        """
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.value
