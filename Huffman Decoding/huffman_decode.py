import binary_search_tree

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
    stuffToPutInPQ = []
    #go through all the characters and their frequencies in steps of 2
    for i in range(0, charStuff, 2):
        #even indices are ASCII codes and odd are their frequencies
        stuffToPutInPQ[i/2] = (charStuff[i], charStuff[i + 1])



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



    #decode/compose the message

    decodedString = ""
    #navigate to the respective character/leaf in the BST (0 = left, 1 = right)
    #add the node's character to the decodedString
    #move to the next binary character


    #You should check the given encoded message to detect errors in the encoding.
    ""
    Hint: use the maximum length of a key to decide that there is an error. If a portion of the encoded
        message is longer than max length of key, and this portion does not exist in the encoding set,
        then this is an error condition.
    ""


    #Use the encoding set/tree to decode the message. The function
    #    returns the decoded message (the original string)
    decodedMessage = ""

    #some function here

    return decodedMessage
    """

def huffman_encode(encoded_message):
    """
    #create an empty dictionary (hash table) for ASCII characters and their frequencies
    characterCounts = {}

    #go through the encoded message
    for character in encoded_message:
        #if there's already a value for the character frequency in the hash table
        if (characterCounts[character] exists):
            #increment the character counter
            characterCounts[character] += 1
        #otherwise if it doesn't exist yet
        else:
            #create it
            characterCounts[character] = 1

    #Now that we have a dictionary of all the characters in the encoded message and their frequencies,
    #put them in a tree
    """