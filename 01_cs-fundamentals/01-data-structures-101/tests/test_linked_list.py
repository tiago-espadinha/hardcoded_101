import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_empty_list(self):
        self.assertEqual(len(self.ll), 0)
        self.assertIsNone(self.ll.head)
        self.assertEqual(self.ll.to_list(), [])
        self.assertFalse(self.ll.delete(10))
        self.assertIsNone(self.ll.search(10))

    def test_prepend(self):
        self.ll.prepend(1)
        self.ll.prepend(2)
        self.assertEqual(self.ll.to_list(), [2, 1])
        self.assertEqual(len(self.ll), 2)

    def test_append(self):
        self.ll.append(1)
        self.ll.append(2)
        self.assertEqual(self.ll.to_list(), [1, 2])
        self.assertEqual(len(self.ll), 2)

    def test_delete(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.assertTrue(self.ll.delete(2))
        self.assertEqual(self.ll.to_list(), [1, 3])
        self.assertTrue(self.ll.delete(1))
        self.assertEqual(self.ll.to_list(), [3])
        self.assertTrue(self.ll.delete(3))
        self.assertEqual(self.ll.to_list(), [])

    def test_search(self):
        self.ll.append(1)
        self.ll.append(2)
        node = self.ll.search(2)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 2)
        self.assertIsNone(self.ll.search(3))

    def test_reverse(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.reverse()
        self.assertEqual(self.ll.to_list(), [3, 2, 1])

    def test_duplicate_insertions(self):
        self.ll.append(1)
        self.ll.append(1)
        self.assertEqual(len(self.ll), 2)
        self.assertTrue(self.ll.delete(1))
        self.assertEqual(len(self.ll), 1)

if __name__ == '__main__':
    unittest.main()
