#return a list of the frequencies of all ascii characters (index is ascii code and value at index is frequency)
"""
example:
    Suppose the file to be encoded contained:   ddddddddddddddddccccccccbbbbaaff
    Numbers in positions of freq counts:        [97:104] = [2, 4, 8, 16, 0, 2, 0]
"""

class HuffmanNode:
    def __init__(self, freq=0, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def isLeaf(self):
        if (self.left is None and self.right is None):
            return True
        else:
            return False

    # get the height of the tree: the length of the path from the root to the farthest leaf node
    def height(self, node):
        # if the bottom of the tree has been reached, return 0
        if (node is None):
            return 0
        else:
            # find the height of each subtree recursively
            lheight = node.height(self.left)
            rheight = node.height(self.right)

            # if the left is longer than the right, use that
            if (lheight > rheight):
                return lheight + 1
            else:
                return rheight + 1

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

#returns true if tree ‘a’ comes before tree ‘b’.
def comes_before(a, b):
    if (a.freq < b.freq):
        return True
    #In case of equal occurrence counts, break the tie by using the ASCII value of the character to determine the order.
    elif ((a.freq == b.freq) and (a.char < b.char)):
        return True
    else:
        return False

def composeHuffTree(huffmanNodeList):
    while (len(huffmanNodeList) > 1):
        adoptiveParent = HuffmanNode()

        # remove the 2 least frequent characters from the priority queue
        leftNode = huffmanNodeList.pop(0)
        rightNode = huffmanNodeList.pop(0)

        # choose the smaller node as the left node and the larger node as the right node if they're not already like that
        if (not comes_before(leftNode, rightNode)):
            temp = leftNode
            leftNode = rightNode
            rightNode = temp

        # create a parent node with a value equal to the sum of the frequencies of the 2 least frequent characters and make it the root of a new BST of the 3 nodes
        adoptiveParent.freq = leftNode.freq + rightNode.freq

        #   make char0 the left node and char
        # since the value of the key for char0 should be smaller to or equal to char1, 1 the right node
        adoptiveParent.left = leftNode
        adoptiveParent.right = rightNode

        # the parent should the ascii character value of the minimum node (copy ascii code of smaller of 2 children)
        adoptiveParent.char = adoptiveParent.left.char

        # insert the new root node/BST with the combined frequency value and character valueinto the list
        # at the right spot
        i = 0
        # while the adoptive parent's is less than the current node in the node list
        while (i < len(huffmanNodeList) and not comes_before(adoptiveParent, huffmanNodeList[i])):
            i += 1
        huffmanNodeList.insert(i, adoptiveParent)

def create_huff_tree(freq_list):
    #create a list of characters with their nonzero frequencies
    # add stuff to the list as a huffman node with its respective key (frequency) and value (char value)
    nonzeroHuffmanNodeList = []
    for charValue in range(128):
        if (freq_list[charValue] != 0):
            nonzeroHuffmanNodeList.append(HuffmanNode(freq_list[charValue], charValue))

    #If freq_list does not contain any non-zero counts (i.e. input file was empty), then create_huff_tree(freq_list) should return None
    if (len(nonzeroHuffmanNodeList) == 0):
        return None
    #If freq_list contains only one non-zero count (i.e. input file has only one unique character),
    # then create_huff_tree(freq_list) should return just the one HuffmanNode containing the character and itsoccurrence count.
    elif (len(nonzeroHuffmanNodeList) == 1):
        return nonzeroHuffmanNodeList[0]

    """
    #for debugging
    huffmanNodeFreqString = ""
    for i in range(len(nonzeroHuffmanNodeList)):
        huffmanNodeFreqString += str(nonzeroHuffmanNodeList[i].freq) + " "
    print(huffmanNodeFreqString)
    """

    #sort the huffman nodes in ascending frequency order
    #lambda input: output
    #lambda x: x.freq == def asdf(x)
    #                        return x.freq
    nonzeroHuffmanNodeList = sorted(nonzeroHuffmanNodeList, key=lambda x: x.freq)

    """
    #for debugging
    huffmanNodeFreqString = ""
    for i in range(len(nonzeroHuffmanNodeList)):
        huffmanNodeFreqString += str(nonzeroHuffmanNodeList[i].freq) + " "
    print(huffmanNodeFreqString)
    """

    #iterate until there's only there's only 1 node left in the loist bruv
    composeHuffTree(nonzeroHuffmanNodeList)
    #print(str(nonzeroHuffmanNodeList[0].freq))

    #return the last remaining element in the list: the root node of the huffman tree
    return nonzeroHuffmanNodeList[0]

def create_header(freq_list):
    """
    takes as parameter the list of freqs previously determined from cnt_freq(filename).
    The create_header function returns a string of the ASCII values and
    their associated frequencies from the input file text, separated by one space.
    For example, create_header(freq_list) would return “97 3 98 4 99 2” for the text “aaabbbbcc”
    """

    header = ""
    for i in range(len(freq_list)):
        if (freq_list[i] != 0):
            header += str(i) + " " + str(freq_list[i] + " ")
    header = header[0:-1]

    return header

def createCode(currentChar, root):
		if(root == None):
			return

        code = ""
        currentNode = root
        while (not currentNode.isLeaf()):
		    if (currentChar < currentNode.char):
                currentNode = currentNode.left
                code += "0"
            else:
                currentNode = currentNode.right
                code += "1"

def create_code(root_node):
    """
    traverses the Huffman tree that was passed as an argument and returns an array (using a Phython list) of 256 strings.
    Use the character’s respective integer ASCII representation as the index into the array, with the resulting Huffman code for thatcharacter stored at that location.
    Traverse the tree from the root to each leaf node and adding a ’0’ when we go ’left’ and a ’1’ when we go ’right’ constructing a string of 0’s and 1’s.
    use the built-in ’+’ operator to concatenate strings of ’0’s and ’1’s here.
    """
    codes = [""] * 256

    for i in range(len(codes)):
        codes[i] = createCode(i, root_node, root_node)

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