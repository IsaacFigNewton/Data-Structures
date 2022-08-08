import unittest
import huffman
import huffman_decode

class MyTestCase(unittest.TestCase):
    def test_cnt_freq(self):
        freqs = [0] * 256
        freqs[65] = 2
        freqs[66] = 2
        freqs[67] = 2
        freqs[68] = 2

        self.assertListEqual(huffman.cnt_freq("abcdabcd.txt"), freqs)

    def test_create_huff_tree(self):
        freqs = huffman.cnt_freq("abcdabcd.txt")
        predictedRoot = huffman.create_huff_tree(freqs)

        expectedRoot = huffman.HuffmanNode(8, 65)
        expectedRoot.left = huffman.HuffmanNode(4, 65)
        expectedRoot.left.left = huffman.HuffmanNode(2, 65)
        expectedRoot.left.right = huffman.HuffmanNode(2, 66)
        expectedRoot.right = huffman.HuffmanNode(4, 67)
        expectedRoot.right.left = huffman.HuffmanNode(2, 67)
        expectedRoot.right.right = huffman.HuffmanNode(2, 68)

        self.assertTrue(predictedRoot.equalTo(expectedRoot))

    def test_create_code(self):
        freqs = huffman.cnt_freq("abcdabcd.txt")
        root = huffman.create_huff_tree(freqs)

        codes = [""] * 256
        codes[65] = "00"
        codes[66] = "01"
        codes[67] = "10"
        codes[68] = "11"

        self.assertEqual(huffman.create_code(root), codes)

    def test_create_header(self):
        freqs = huffman.cnt_freq("abcdabcd.txt")
        root = huffman.create_huff_tree(freqs)

        self.assertEqual(huffman.create_header(freqs), "65 2 66 2 67 2 68 2")

    def test_huffman_encode(self):
        #Empty test file

        #create the file
        inputFile = open("empty_file.txt", "w")
        inputFile.close()

        #encode and test it
        huffman.huffman_encode("empty_file.txt", "empty_file_out.txt")
        outputFile = open("empty_file_out.txt", "r")
        output = outputFile.read()
        outputFile.close()
        self.assertEqual(output, "\n")


        #AAAAA
        huffman.huffman_encode("5a.txt", "5a_out.txt")
        outputFile = open("5a_out.txt", "r")
        output = outputFile.read()
        outputFile.close()
        self.assertEqual(output, "97 5\n11111")


        #ABCDABCD
        huffman.huffman_encode("abcdabcd.txt", "abcdabcd_out.txt")
        outputFile = open("abcdabcd_out.txt", "r")
        output = outputFile.read()
        outputFile.close()
        self.assertEqual(output, "65 2 66 2 67 2 68 2\n0001101100011011")


        #entire bee movie script

        #save the script to a variable
        inputFile = open("bee_movie.txt", "r")
        beeMovie = inputFile.read()
        inputFile.close()

        #encode and test it
        huffman.huffman_encode("bee_movie.txt", "bee_movie_out.txt")
        outputFile = open("bee_movie_out.txt", "r")
        output = outputFile.read()
        outputFile.close()
        self.assertEqual(huffman_decode.huffman_decode(output), beeMovie)



if __name__ == '__main__':
    unittest.main()
