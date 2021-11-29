#return a list of the frequencies of all ascii characters (index is ascii code and value at index is frequency)
"""
example:
    Suppose the file to be encoded contained:   ddddddddddddddddccccccccbbbbaaff
    Numbers in positions of freq counts:        [97:104] = [2, 4, 8, 16, 0, 2, 0]
"""
def cnt_freq(filename):
    #can you open and read a file in the same line?
    inFile = open(filename, "r").read

    #use only the body of the input file, not the header (legend of ascii characters and their binary codes)
    dividerIndex = inFile.index("\n")
    message = inFile[0:dividerIndex]

    freqs = [0] * 256
    #increment the frequency (occurrence count) at every character's respective index in the frequency list
    for char in message:
        freqs[int(char)] += 1

    return freqs


def create_header(freq_list):
    """
    takes as parameter the list of freqs previously determined from cnt_freq(filename).
    The create_header function returns a string of the ASCII values and
    their associated frequencies from the input file text, separated by one space.
    For example, create_header(freq_list) would return “97 3 98 4 99 2” for the text “aaabbbbcc”
    """

    """

    """
    return ""

def create_code(root_node):
    """
    We have completed our Huffman tree, but we are still lacking a way to get our Huffman codes.
    Implement a function namedcreate_code(root_node) that traverses the Huffman tree that was passedas an argument and returns an array (using a Phython list) of 256 strings.
    Use the character’s respectiveinteger ASCII representation as the index into the arrary, with the resulting Huffman code for thatcharacter stored at that location.
    Traverse the tree from the root to each leaf node and adding a ’0’ whenwe go ’left’ and a ’1’ when we go ’right’ constructing a string of 0’s and 1’s.
    use the built-in ’+’ operator to concatenate strings of ’0’s and ’1’s here.
    """
    codes = [""] * 256

    """

    """

    return codes

#open files with
def huffman_encode(in_file, out_file):
    #can you open and read a file in the same line?
    message = open(in_file, "r").read

    #make a new list of every ascii character (index in list) and its frequency (value at index)
    charFreqs = cnt_freq(in_file)

    #build the huffman tree
    huffmanTree = create_huff_tree(charFreqs)

    #make a new list of every ascii character (index in list) and their binary encoding (value at index)
    codes = create_code(huffmanTree.root)

    #read the message to be encoded and for every character,
    #go to the encoding in the codesLegend
    #and compose an encoded string with the binary code stored there
    encodedMessage = ""
    for char in message:
        encodedMessage += codes[int(char)]

    #write the header to the out_file
    open(out_file, 'w', create_header(charFreqs))
    #add a new line
    open(out_file, 'a', newline='')
    #write the encodedMessage to the out_file
    open(out_file, 'a', encodedMessage)