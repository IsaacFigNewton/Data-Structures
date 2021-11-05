import unittest
import bin_heap

#Important to note: The one failed test case is because of the raised exception MyException
class MyTestCase(unittest.TestCase):
    def test_insert(self):
        print("Running test_insert")
        heap = bin_heap.BinHeap(8)

        heap.insert(7)
        heap.insert(5)
        heap.insert(4)
        heap.insert(9)
        heap.insert(1)
        heap.insert(15)
        heap.insert(32)
        heap.insert(26)
        #the list should expand here
        heap.insert(54)
        heap.insert(3)
        heap.insert(17)
        heap.insert(69)

        self.assertEqual(heap.elements[1], 1)
        self.assertEqual(heap.elements[2], 3)
        self.assertEqual(heap.elements[3], 5)
        self.assertEqual(heap.elements[4], 9)
        self.assertEqual(heap.elements[5], 4)
        self.assertEqual(heap.elements[6], 15)
        self.assertEqual(heap.elements[7], 32)
        self.assertEqual(heap.elements[8], 26)
        self.assertEqual(heap.elements[9], 54)
        self.assertEqual(heap.elements[10], 7)
        self.assertEqual(heap.elements[11], 17)
        self.assertEqual(heap.elements[12], 69)
        print()

    def test_deleteMin_isEmpty_size(self):
        print("Running test_deleteMin_isEmpty_size")
        heap = bin_heap.BinHeap(8)

        self.assertEqual(heap.size(), 0)
        self.assertTrue(heap.isEmpty())

        heap.insert(7)
        heap.insert(5)
        heap.insert(4)
        heap.insert(9)

        self.assertFalse(heap.isEmpty())
        self.assertEqual(heap.size(), 4)

        heap.insert(1)
        heap.insert(15)
        heap.insert(32)
        heap.insert(26)

        self.assertEqual(heap.deleteMin(), 1)
        self.assertEqual(heap.deleteMin(), 4)
        self.assertEqual(heap.deleteMin(), 5)
        self.assertEqual(heap.deleteMin(), 7)

        self.assertFalse(heap.isEmpty())
        self.assertEqual(heap.size(), 4)

        self.assertEqual(heap.deleteMin(), 9)
        self.assertEqual(heap.deleteMin(), 15)
        self.assertEqual(heap.deleteMin(), 26)
        self.assertEqual(heap.deleteMin(), 32)

        self.assertEqual(heap.size(), 0)
        self.assertTrue(heap.isEmpty())
        print()

    def test_MyException(self):
        print("Running test_MyException")
        heap = bin_heap.BinHeap(4)

        heap.insert(7)
        heap.insert(5)
        heap.insert(4)
        heap.insert(9)

        heap.deleteMin()
        heap.deleteMin()
        heap.deleteMin()
        heap.deleteMin()
        heap.deleteMin()

    def test__string__(self):
        print("Running test__string__")
        heap = bin_heap.BinHeap(8)

        heap.insert(7)
        heap.insert(5)
        heap.insert(4)
        heap.insert(9)
        heap.insert(1)
        heap.insert(15)
        heap.insert(32)
        heap.insert(26)

        heap.__string__()
        print("")
if __name__ == '__main__':
    unittest.main()
