import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_empty_stack(self):
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
        with self.assertRaises(IndexError):
            self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_push_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.is_empty())

    def test_single_element(self):
        self.stack.push(10)
        self.assertEqual(self.stack.pop(), 10)
        self.assertTrue(self.stack.is_empty())

if __name__ == '__main__':
    unittest.main()
