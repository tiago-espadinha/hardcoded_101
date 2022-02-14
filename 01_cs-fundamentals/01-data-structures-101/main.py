from linked_list import LinkedList
from doubly_linked_list import DoublyLinkedList
from stack import Stack
from queue_ds import Queue
from bst import BST
from hash_map import HashMap

def demo_linked_list():
    print("===== Linked List =====")
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.prepend(5)
    print(f"List: {ll}")
    print(f"Search 20: {ll.search(20).value}")
    ll.reverse()
    print(f"Reversed: {ll}")
    ll.delete(10)
    print(f"Deleted 10: {ll}")
    print()

def demo_doubly_linked_list():
    print("===== Doubly Linked List =====")
    dll = DoublyLinkedList()
    dll.append(100)
    dll.prepend(50)
    dll.append(150)
    print(f"List: {dll}")
    dll.delete(100)
    print(f"Deleted 100: {dll}")
    print()

def demo_stack():
    print("===== Stack =====")
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"Stack: {s}")
    print(f"Pop: {s.pop()}")
    print(f"Peek: {s.peek()}")
    print(f"Size: {s.size()}")
    print()

def demo_queue():
    print("===== Queue =====")
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(f"Queue: {q}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Peek: {q.peek()}")
    print(f"Size: {q.size()}")
    print()

def demo_bst():
    print("===== Binary Search Tree =====")
    tree = BST()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(val)
    print(f"Inorder: {tree.inorder()}")
    print(f"Height: {tree.height()}")
    print(f"Search 40: {tree.search(40)}")
    print(f"Min: {tree.min_value()}, Max: {tree.max_value()}")
    tree.delete(50)
    print(f"Deleted root (50). New Inorder: {tree.inorder()}")
    print()

def demo_hash_map():
    print("===== Hash Map =====")
    hm = HashMap(initial_capacity=4)
    hm.set("user1", "Tiago")
    hm.set("user2", "Alice")
    hm.set("user3", "Bob")
    print(f"Keys: {hm.keys()}")
    print(f"Get user2: {hm.get('user2')}")
    hm.set("user4", "Charlie") # Should trigger resize
    print(f"Capacity after 4th element: {hm.capacity}")
    print(f"All items: {hm.items()}")
    print()

if __name__ == "__main__":
    demo_linked_list()
    demo_doubly_linked_list()
    demo_stack()
    demo_queue()
    demo_bst()
    demo_hash_map()
