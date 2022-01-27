import unittest
from bst import BST

class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def test_empty_bst(self):
        self.assertFalse(self.bst.search(10))
        self.assertEqual(self.bst.inorder(), [])
        self.assertEqual(self.bst.height(), 0)
        self.assertIsNone(self.bst.min_value())

    def test_insert_search(self):
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.assertTrue(self.bst.search(30))
        self.assertTrue(self.bst.search(70))
        self.assertFalse(self.bst.search(10))

    def test_traversals(self):
        # Balanced tree
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(70)
        self.bst.insert(60)
        self.bst.insert(80)
        
        self.assertEqual(self.bst.inorder(), [20, 30, 40, 50, 60, 70, 80])
        self.assertEqual(self.bst.preorder(), [50, 30, 20, 40, 70, 60, 80])
        self.assertEqual(self.bst.postorder(), [20, 40, 30, 60, 80, 70, 50])

    def test_delete(self):
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.delete(30)
        self.assertFalse(self.bst.search(30))
        self.assertEqual(self.bst.inorder(), [50, 70])
        
        self.bst.delete(50)
        self.assertEqual(self.bst.inorder(), [70])

    def test_skewed_trees(self):
        # Right skewed
        rbst = BST()
        rbst.insert(10)
        rbst.insert(20)
        rbst.insert(30)
        self.assertEqual(rbst.height(), 3)
        self.assertEqual(rbst.inorder(), [10, 20, 30])
        
        # Left skewed
        lbst = BST()
        lbst.insert(30)
        lbst.insert(20)
        lbst.insert(10)
        self.assertEqual(lbst.height(), 3)
        self.assertEqual(lbst.inorder(), [10, 20, 30])

    def test_min_max(self):
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.assertEqual(self.bst.min_value(), 30)
        self.assertEqual(self.bst.max_value(), 70)

if __name__ == '__main__':
    unittest.main()
