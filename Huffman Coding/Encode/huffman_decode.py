#I was supposed to use a PQ for composing the huffman tree

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

def parseFreqs(header):
    #get an array of strings representing the ASCII codes and their frequencies
    charStuff = header.split(" ")

    #go through all the characters and their frequencies and convert them from strings to int types
    charStuff = list(map(int, charStuff))

    #make a new list of every ascii character (index in list) and its frequency (value at index)
    charFreqs = [0] * 256

    #go through all the characters and their frequencies
    for i in range(0, len(charStuff) - 1, 2):
        #even indices in charStuff are ASCII codes and odd are their frequencies
        charFreqs[charStuff[i]] = charStuff[i + 1]

    return charFreqs

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

def decodeBinaryWithTree(binary, root):
    decodedString = ""
    currentNode = root
    maxKeyLength = root.height(root)
    currentKeyLength = 0

    # read every bit in the encoded message
    for bitIndex in range(len(binary)):
        bit = binary[bitIndex]

        currentKeyLength += 1
        # if the current code/key length not exist in the encoding set (it's longer than any real path),
        #   then there is a mistake in the encoded message
        if (currentKeyLength > maxKeyLength):
            print("There was a mistake in the input message's encoding.")

        # move to the projenitor (character or not)
        if (currentNode.left != None and bit == "0"):
            currentNode = currentNode.left
        elif (currentNode.right != None):
            currentNode = currentNode.right

        # if it's a leaf, add the character to the decoded string and start over
        if (currentNode.isLeaf()):
            decodedString += chr(currentNode.char)
            currentNode = root

            currentKeyLength = 0

    return decodedString

#example of encoded_message: “65 3 66 1 67 4 68 2\n1110001011111000101”
def huffman_decode(encoded_message):
    # if there was no encoded message
    if (len(encoded_message) < 2):
        return ""

    #separate the head and the body into 2 strings
    splitMessage = encoded_message.split("\n")
    header = splitMessage[0]
    body = splitMessage[1]

    #for debugging
    #print("encoded message header: " + header)
    #print("encoded message body: " + body)

    #get the character frequencies
    charFreqs = parseFreqs(header)

    """
    #for debugging
    charString = "characters: ["
    for i in range(256):
        charString += str(i) + " "
    charString = charString[0: -1]
    print(charString + "]")
    print("frequencies: " + str(charFreqs))
    """

    #build the huffman tree
    huffmanTreeRoot = create_huff_tree(charFreqs)

    return decodeBinaryWithTree(body, huffmanTreeRoot)