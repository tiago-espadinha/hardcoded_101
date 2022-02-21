import unittest
from queue_ds import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_empty_queue(self):
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)
        with self.assertRaises(IndexError):
            self.queue.dequeue()
        with self.assertRaises(IndexError):
            self.queue.peek()

    def test_enqueue_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)
        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertTrue(self.queue.is_empty())

    def test_single_element(self):
        self.queue.enqueue(10)
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertTrue(self.queue.is_empty())

if __name__ == '__main__':
    unittest.main()
