import binary_search_tree

#huffman tree should be its own class

def parseFreqs(header):
    #get an array of strings representing the ASCII codes and their frequencies
    charStuff = header.split(" ")

    #go through all the characters and their frequencies and convert them from strings to int types
    charStuff = list(map(int, charStuff))

    #make a new list of every ascii character (index in list) and its frequency (value at index)
    charFreqs = [0] * 256

    #go through all the characters and their frequencies
    for i in range(0, charStuff, 2):
        #even indices in charStuff are ASCII codes and odd are their frequencies
        charFreqs[charStuff[i]] = charStuff[i + 1]

    return charFreqs

def create_huff_tree(freq_list):

    #create a list of characters with their nonzero frequencies
    nonzeroFreqs = []
    for i in range(128):
        if (freq != 0):
            nonzeroFreqs.append((i, freq_list[i]))

    #If freq_list does not contain any non-zero counts (i.e. input file was empty), then create_huff_tree(freq_list) should return None
    if (len(nonzeroFreqs) == 0):
        return None
    #If freq_list contains only one non-zero count (i.e. input file has only one unique character),
    # then create_huff_tree(freq_list) should return just the one HuffmanNode containing the character and itsoccurrence count.
    elif (len(nonzeroFreqs) == 1):
        return HuffmanNode(nonzeroFreqs[0][0], nonzeroFreqs[0][1])

    """
    #You should build the Huffman tree from the header to get the encoding set (the code words
    #    representing the characters)

    #create a priority queue with the ASCII characters and their frequencies
    charFreqPQ = binary_heap.BinaryHeap()
    for charValue in range(len(freq_list)):
        #add stuff to the PQ as a huffman nodewith its respective key (frequency) and value (char value)
        charFreqPQ.enqueue(huffmanNode(freq_list, charValue))

    #iterate until there's only there's only 1 node left in the priority queue, aka, if the BST has finished being created
    while (charFreqPQ.size >= 2 nodes):
        #remove the 2 least frequent characters from the priority queue
        node0 = charFreqPQ.dequeue()
        node1 = charFreqPQ.dequeue()

        #create a parent node with a value equal to the sum of the frequencies of the 2 least frequent characters and make it the root of a new BST of the 3 nodes
        adoptiveParent = node0.key + node1.key
        
        #the parent should also have the minimum of the left and right character representations stored in it in order to resolve ties in the comes_before() function.
        adoptiveParent.minLeft = node0.minLeft
        adoptiveParent.minRight = node1.minLeft
        
        #since the value of the key for char0 should be smaller to or equal to char1,
        #   make char0 the left node and char 1 the right node
        adoptiveParent.left = node0
        adoptiveParent.right = node1

        #insert the new root node/BST with the combined frequency value into the priority queue
        
    #return the last remaining element in the pq: the root node of the huffman tree
    return charFreqPQ.dequeue()
    """

def decodeMessageWithTree(binary, tree):
    # Use the encoding set/tree to decode the message.
    decodedString = ""
    currentNode = tree.root
    maxKeyLength = tree.getHeight()
    currentKeyLength = 0

    # read every bit in the encoded message
    for bitIndex in range(len(binary)):
        # get the bit
        bit = message[bitIndex]

        currentKeyLength += 1
        # if the current code/key length not exist in the encoding set (it's longer than any real path),
        #   then there is a mistake in the encoded message
        if (currentKeyLength > maxKeyLength):
            print("There was a mistake in the input message's encoding.")

        # move to the projenitor (character or not)
        if (bit == "0"):
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right

        # if it's a leaf, add the character to the decoded string and start over
        if (isLeaf(currentNode)):
            decodedString += currentNode.char
            currentNode = tree.root

            currentKeyLength = 0

        return decodedString

#example of encoded_message: “65 3 66 1 67 4 68 2\n1110001011111000101”
def huffman_decode(encoded_message):
    #separate the head and the body into 2 strings
    splitMessage = encoded_message.split("\n")
    header = splitMessage[0]
    body = splitMessage[1]

    #get the character frequencies
    charFreqs = parseFreqs(header)

    #build the huffman tree
    huffmanTree = create_huff_tree(charFreqs)

    return decodeBinaryWithTree(body, huffmanTree)












#return a list of the frequencies of all ascii characters (index is ascii code and value at index is frequency)
"""
example: 
    Suppose the file to be encoded contained:   ddddddddddddddddccccccccbbbbaaff
    Numbers in positions of freq counts:        [97:104] = [2, 4, 8, 16, 0, 2, 0]
"""
def cnt_freq(filename):
    #can you open and read a file in the same line?
    inFile = open(in_file, "r").read

    #use only the body of the input file, not the header (legend of ascii characters and their binary codes)
    dividerIndex = inFile.index("\n")
    message = inFile[0:dividerIndex]

    freqs = [0] * 256
    #increment the frequency (occurrence count) at every character's respective index in the frequency list
    for char in message:
        freqs[(int)char] += 1

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
        encodedMessage += codes[(int)char]

    #write the header to the out_file
    open(out_file, 'w', create_header(charFreqs))
    #add a new line
    open(out_file, 'a', newline='')
    #write the encodedMessage to the out_file
    open(out_file, 'a', encodedMessage)