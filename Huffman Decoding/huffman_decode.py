import binary_search_tree






#note: be better than me, remove the offsets; they're unnecessary,
# also, a huffman tree should be its own class, distinct from a regular BST





#return a list of the frequencies of all ascii characters
def cnt_freq(message):
    """

    """
    return []

def buildHuffmanTree(stuffToPutInPQ):
    """

    #You should build the Huffman tree from the header to get the encoding set (the code words
    #    representing the characters)

    #create a priority queue with the ASCII characters and their frequencies
    charFreqPQ = binary_heap.BinaryHeap()
    for tuple in stuffToPutInPQ:
        #add stuff to the PQ with its respetive key and value
        charFreqPQ.enqueue(tuple[0], tuple[1])

    #iterate until there's only there's only 1 node left in the priority queue, aka, if the BST has finished being created
    while (priority queue size >= 2 nodes):
        #remove the 2 least frequent characters from the priority queue
        char1 = charFreqPQ.dequeue
        char2 = charFreqPQ.dequeue
        #create a node with a value equal to the sum of the frequencies of the 2 least frequent characters and make it the root of a new BST of the 3 nodes

        #insert the new root node/BST with the combined frequency value into the priority queue

    return huffmanTree
    """

# decode/compose a binary string with a huffman tree
def decodeWithStuff(binaryString, BST):
    """
    decodedString = ""
    #navigate to the respective character/leaf in the BST (0 = left, 1 = right)
    #You should check the given encoded message to detect errors in the encoding.
    ""
    Hint: use the maximum length of a key to decide that there is an error. If a portion of the encoded
        message is longer than max length of key, and this portion does not exist in the encoding set,
        then this is an error condition.
    ""

    #add the node's character to the decodedString

    #move to the next binary character
    """
    return decodedString

#example of encoded_message: “65 3 66 1 67 4 68 2\n1110001011111000101”
def huffman_decode(encoded_message):
    """
    #separate the head and the body into 2 strings
    splitMessage = encoded_message.split("\n")
    headString = splitMessage[0]
    bodyString = splitMessage[1]

    #get an array of strings representing the ASCII codes and their frequencies
    charStuff = headString.split(" ")

    #go through all the characters and their frequencies and convert them from strings to int types
    charStuff = list(map(int, charStuff))

    #make a new list of tuples with the first index of each representing the ASCII code
    #and the second representing the frequency
    stuffToPutInTree = []
    #go through all the characters and their frequencies in steps of 2
    for i in range(0, charStuff, 2):
        #even indices are ASCII codes and odd are their frequencies
        stuffToPutInTree[i/2] = (charStuff[i], charStuff[i + 1])

    #build the huffman tree
    huffmanTree = buildHuffmanTree(stuffToPutInTree)

    #Use the encoding set/tree to decode the message. The function
    #    returns the decoded message (the original string)
    return decodeWithStuff(bodyString, huffmanTree)
    """












#example of output: {32:00, 33:10, 34:11, 35:010} (ascii offset is 32)
def huffmanTreeCodesToHashtable(huffmanTree):
    """
    #the dictionary of binary codes for every ascii character in the huffmanTree
    listOfCodes = {}

    """

#example of output: [3, 1, 4, 0, 2] (ascii offset is 32)
def huffmanTreeToList(huffmanTree):
    """
    listOfFrequencies
    """

def huffman_encode(message):
    """
    #for getting the frequencies of all ascii characters,
    #save for command ones, like NULL and CARRIAGE_RETURN, so start at ASCII code 32
    offset = 32

    #make a list of the frequencies of all ascii characters in the original message
    #(indice is ascii code - offset)
    charFrequencies = [0]*(127 - offset)


    #compose the list of tuples of character frequencies and their codes to put in the huffman tree (frequency is key)
    stuffToPutInTree = []
    for i in range(len(charFrequencies)):
        #if the ascii character in question had at least 1 occurrence
        if (charFrequencies[i] > 0):
            stuffToPutInTree[i] = (charFrequencies[i], i + offset)

    huffmanTree = buildHuffmanTree(stuffToPutInTree)

    #somehow convert the huffman tree to a dictionary of ascii codes and their binary encodings
    codesLegend = huffmanTreeCodesToList(huffmanTree)

    #read the message to be encoded and for every character,
    #go to the encoding in the codesLegend
    #and replace the character with the binary code stored there
    encodedMessage = ""


    #convert the legend to a string of the format “65 3 66 1 67 4 68 0 69(nice) 2"
    frequenciesLegend = huffmanTreeToList(huffmanTree)
    frequenciesLegendString = ""
    for i in range(len(frequenciesLegend)):
        #you know what to put here

    combinedString = legendString + "\n" + encodedMessage

    return combinedString

    """