import unittest
from doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_empty_list(self):
        self.assertEqual(len(self.dll), 0)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(self.dll.to_list(), [])
        self.assertFalse(self.dll.delete(10))
        self.assertIsNone(self.dll.search(10))

    def test_prepend(self):
        self.dll.prepend(1)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.tail.value, 1)
        self.dll.prepend(2)
        self.assertEqual(self.dll.to_list(), [2, 1])
        self.assertEqual(self.dll.head.value, 2)
        self.assertEqual(self.dll.tail.value, 1)
        self.assertEqual(len(self.dll), 2)

    def test_append(self):
        self.dll.append(1)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.tail.value, 1)
        self.dll.append(2)
        self.assertEqual(self.dll.to_list(), [1, 2])
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.tail.value, 2)
        self.assertEqual(len(self.dll), 2)

    def test_delete(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertTrue(self.dll.delete(2))
        self.assertEqual(self.dll.to_list(), [1, 3])
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.tail.value, 3)
        
        self.assertTrue(self.dll.delete(1))
        self.assertEqual(self.dll.head.value, 3)
        self.assertEqual(self.dll.tail.value, 3)
        
        self.assertTrue(self.dll.delete(3))
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(len(self.dll), 0)

    def test_search(self):
        self.dll.append(1)
        self.dll.append(2)
        node = self.dll.search(2)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 2)
        self.assertEqual(node.prev.value, 1)
        self.assertIsNone(self.dll.search(3))

if __name__ == '__main__':
    unittest.main()
