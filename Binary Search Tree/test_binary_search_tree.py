import unittest
import binary_search_tree

class MyTestCase(unittest.TestCase):
    def test_find_min(self):
        print("\n")
        print("Running test_find_main")

        tree = binary_search_tree.BinarySearchTree()

        # level 0
        tree.insert(7)
        # level 1
        tree.insert(3)
        tree.insert(11)
        # level 2
        tree.insert(2)
        tree.insert(4)
        tree.insert(24)
        tree.insert(12)  #level 3
        tree.insert(8)

        self.assertEqual(tree.find_min(tree.root).key, 2)

    def test_find_max(self):
        print("\n")
        print("Running test_find_max")

        tree = binary_search_tree.BinarySearchTree()

        # level 0
        tree.insert(7)
        # level 1
        tree.insert(3)
        tree.insert(11)
        # level 2
        tree.insert(2)
        tree.insert(4)
        tree.insert(24)
        tree.insert(12)  #level 3
        tree.insert(8)

        self.assertEqual(tree.find_max(tree.root).key, 24)

    def test_height(self):
        print("\n")
        print("Running test_height")

        tree = binary_search_tree.BinarySearchTree()

        # level 0
        tree.insert(7)
        self.assertEqual(tree.height(tree.root), 1)

        # level 1
        tree.insert(3)
        tree.insert(11)
        self.assertEqual(tree.height(tree.root), 2)

        # level 2
        tree.insert(2)
        tree.insert(4)
        tree.insert(24)
        self.assertEqual(tree.height(tree.root), 3)

        tree.insert(12)  #level 3
        tree.insert(8)
        self.assertEqual(tree.height(tree.root), 4)

    def test_insert(self):
        print("\n")
        print("Running test_insert")

        tree = binary_search_tree.BinarySearchTree()

        #level 0
        tree.insert(7)
        #level 1
        tree.insert(3)
        tree.insert(11)
        #level 2
        tree.insert(2)
        tree.insert(4)
        tree.insert(24)
        tree.insert(12) #level 3
        tree.insert(8)

        #level 0
        self.assertEqual(tree.root.key, 7)
        #level 1
        self.assertEqual(tree.root.left.key, 3)
        self.assertEqual(tree.root.right.key, 11)
        #level 2
        self.assertEqual(tree.root.left.left.key, 2)
        self.assertEqual(tree.root.left.right.key, 4)
        self.assertEqual(tree.root.right.left.key, 8)
        self.assertEqual(tree.root.right.right.key, 24)
        self.assertEqual(tree.root.right.right.left.key, 12)

    def test_delete(self):
        print("\n")
        print("Running test_delete")

        tree = binary_search_tree.BinarySearchTree()

        #level 0
        tree.insert(7)
        #level 1
        tree.insert(3)
        tree.insert(11)
        #level 2
        tree.insert(2)
        tree.insert(4)
        tree.insert(24)
        tree.insert(12) #level 3
        tree.insert(8)

        print("Before deletions")
        tree.print_levels()
        tree.delete(11)
        print("Removed 11")
        tree.print_levels()
        tree.delete(2)
        print("Removed 2")
        tree.print_levels()
        tree.delete(12)
        print("Removed 12")
        tree.print_levels()
        tree.delete(7)
        print("Removed 7")
        tree.print_levels()

        #level 0
        self.assertEqual(tree.root.key, 4)
        #level 1
        self.assertEqual(tree.root.left.key, 3)
        self.assertEqual(tree.root.right.key, 8)
        #level 2
        self.assertEqual(tree.root.right.right.key, 24)

    def test_is_empty(self):
        print("\n")
        print("Running test_is_empty")

        tree = binary_search_tree.BinarySearchTree()

        self.assertTrue(tree.is_empty())

        #level 0
        tree.insert(7)
        #level 1
        tree.insert(3)
        tree.insert(11)
        #level 2
        tree.insert(2)
        tree.insert(4)
        tree.insert(24)
        tree.insert(12) #level 3
        tree.insert(8)

        tree.print_levels()
        tree.delete(11)
        print("removed 11")
        tree.print_levels()
        tree.delete(2)
        print("removed 2")
        tree.print_levels()
        tree.delete(12)
        print("removed 12")
        tree.print_levels()
        tree.delete(7)
        print("removed 7")
        tree.print_levels()
        tree.delete(3)
        print("removed 3")
        tree.print_levels()
        tree.delete(4)
        print("removed 4")
        tree.print_levels()
        tree.delete(24)
        print("removed 24")
        tree.print_levels()
        tree.delete(8)
        print("removed 8")
        tree.print_levels()

        print(str(tree.keys))

        self.assertTrue(tree.is_empty())

    def test_findWithKey(self):
        print("\n")
        print("Running test_findWithKey")

        tree = binary_search_tree.BinarySearchTree()

        # level 0
        tree.insert(7)
        # level 1
        tree.insert(3)
        tree.insert(11)
        # level 2
        tree.insert(2)
        tree.insert(4)
        tree.insert(24)
        tree.insert(12)  #level 3
        tree.insert(8)

        self.assertTrue(tree.findWithKey(4))
        self.assertFalse(tree.findWithKey(5))

    def test_inorder_print_tree(self):
        print("\n")
        print("Running test_inorder_print_tree")

        tree = binary_search_tree.BinarySearchTree()

        # level 0
        tree.insert(7)
        # level 1
        tree.insert(3)
        tree.insert(11)
        # level 2
        tree.insert(2)
        tree.insert(4)
        tree.insert(24)
        tree.insert(12)  #level 3
        tree.insert(8)

        tree.inorder_print_tree(tree.root)

    def test_print_levels(self):
        print("\n")
        print("Running test_print_levels")

        tree = binary_search_tree.BinarySearchTree()

        # level 0
        tree.insert(7)
        # level 1
        tree.insert(3)
        tree.insert(11)
        # level 2
        tree.insert(2)
        tree.insert(4)
        tree.insert(24)
        tree.insert(12)  #level 3
        tree.insert(8)

        tree.print_levels()

if __name__ == '__main__':
    unittest.main()