import unittest
import huffman

class MyTestCase(unittest.TestCase):
    def test_something(self):
        huffman.huffman_encode("file1.txt", "file1-out.txt")
        outputFile = open("file1-out.txt", "r")
        output = outputFile.read()
        print(output)
        #self.assertEqual(output, "65 2 66 2 67 2 68 2\n0001101100011011")
        outputFile.close()


if __name__ == '__main__':
    unittest.main()
