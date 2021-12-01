import unittest
import huffman_decode


class MyTestCase(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(huffman_decode.huffman_decode(""), "")
        self.assertEqual(huffman_decode.huffman_decode("65 30\n" + "1" * 30), "A" * 30)
        self.assertEqual(huffman_decode.huffman_decode("65 2 66 2 67 2 68 2\n0001101100011011"), "ABCDABCD")
        self.assertEqual(huffman_decode.huffman_decode("65 3 66 1 67 4 68 2\n1011001111010000111"), "ABCDAACCCD")
        self.assertEqual(huffman_decode.huffman_decode("65 30\n" + "1" * 30), "A" * 30)


if __name__ == '__main__':
    unittest.main()
