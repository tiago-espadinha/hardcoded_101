import unittest
from hash_map import HashMap

class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hm = HashMap(initial_capacity=4)

    def test_empty_hashmap(self):
        self.assertEqual(len(self.hm), 0)
        self.assertIsNone(self.hm.get("nonexistent"))
        self.assertFalse("key" in self.hm)

    def test_set_get(self):
        self.hm.set("name", "Alice")
        self.hm.set("age", 30)
        self.assertEqual(self.hm.get("name"), "Alice")
        self.assertEqual(self.hm.get("age"), 30)
        
        # Update
        self.hm.set("name", "Bob")
        self.assertEqual(self.hm.get("name"), "Bob")

    def test_delete(self):
        self.hm.set("name", "Alice")
        self.assertTrue(self.hm.delete("name"))
        self.assertIsNone(self.hm.get("name"))
        self.assertFalse(self.hm.delete("nonexistent"))

    def test_resize(self):
        # Initial capacity is 4, threshold 0.75 -> resize at >3 items
        self.hm.set("a", 1)
        self.hm.set("b", 2)
        self.hm.set("c", 3)
        initial_cap = self.hm.capacity
        self.hm.set("d", 4)
        self.assertGreater(self.hm.capacity, initial_cap)
        self.assertEqual(self.hm.get("a"), 1)
        self.assertEqual(self.hm.get("d"), 4)

    def test_keys_values_items(self):
        self.hm.set("a", 1)
        self.hm.set("b", 2)
        self.assertIn("a", self.hm.keys())
        self.assertIn(1, self.hm.values())
        self.assertIn(("a", 1), self.hm.items())

if __name__ == '__main__':
    unittest.main()
