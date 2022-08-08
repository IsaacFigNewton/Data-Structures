class MyHashTable:
    """
    this function takes no parameters and returns a MyHashTable object,
    having initialized an empty hash table. The table_size parameter (default value of 11) is the starting size
    of the table (number of “slots” in the table). This function should initialize the hash table (use a Python
    list) and any other instance variables used in your MyHashTable class (e.g. num_items, num_collisions).
    """
    def __init__(self, size = 11, maxCollisions = 2):
        self.maxCollisions = maxCollisions
        self.tableSize = size
        self.collisionCount = 0
        self.table = [[]] * size
        self.num_elements = 0

    """
    this function takes a key, and an item. Keys are valid Python non-negative
    integers. The function will insert the key-item pair into the hash table based on the hash value of the
    key mod the table size (hash_value = key % table_size). If the key-item pair being inserted into the hash
    table is a duplicate key, the old key-item pair will be replaced by the new key-item pair. If the insert
    would cause the load factor of the hash table to become greater than 1.5, the number of slots in the hash
    table should be increased to twice the old number of slots, plus 1 (new_size = 2*old_size + 1). After
    creating the new hash table, the items in the old hash table need to be rehashed into the new table.
    """
    #every key should be unique and self should be a MyHashTable object
    def insert(self, key, item):
        if (self.loadFactor() < 1.5):
            ableToInsert = False

            print("index of collisionList in hash table: " + str(self.hash(key, self.tableSize)))
            print("size of hash table: " + str(self.tableSize))
            print(self.toString())

            #check to make sure the hash of the key is within the table,
            #and if it isn't, expand the table
            if (self.hash(key, self.tableSize) >= self.tableSize):
                self.expandTable()
                self.insert(key, item)
                return

            print("index of collisionList in hash table: " + str(self.hash(key, self.tableSize)))
            print("size of hash table: " + str(self.tableSize))
            print(self.toString())

            #if the length of the collision list is able to accomodate the item and its key
            lengthOfCollisionList = len(self.table[self.hash(key, self.tableSize)])

            #if there are no elements in the collisionList, then just add the item
            if (lengthOfCollisionList == 0):
                #for some reason this inserts the (key, item) pair in every collisionList
                self.table[self.hash(key, self.tableSize)] = [(key, item)]
                self.num_elements += 1

            #check if there's space in the collision list before adding the new element
            elif (lengthOfCollisionList < self.maxCollisions):
                #there was at least one element in the collisionList, so count it as a collision
                self.collisionCount += 1

                #check the collisions in the collisionList for duplicates
                for tupleIndex in range(0, lengthOfCollisionList):
                    tuple = self.table[self.hash(key, self.tableSize)][tupleIndex]

                    #if one of the collisions is a duplicate of the current insertion,
                    #just ignore it and don't change anything
                    if (tuple[0] == key):
                        return

                #if there were no duplicates,
                #just add the item to the end of the respective collisionList based on the key's hash value
                self.table[self.hash(key, self.tableSize)].insert(lengthOfCollisionList - 1, (key, item))
                self.num_elements += 1

            #if there was no space left in the collisionList
            else:
                self.collisionCount += 1
                self.expandTable()
                self.insert(key, item)

        #if self.loadFactor() >= 1.5
        else:
            self.expandTable()
            self.insert(key, item)

    def isPrime(self, num):
        #if it's 1 or 2, it's prime
        if (num == 1 or num == 2):
            return True

        #see if the number has any factors other than 1, up to value/2
        for i in range(2, int(num/2) + 1):
            if (num % i == 0):
                return False

        #if it had no factors other than 1, it is prime
        return True

    def expandTable(self):
        # preserve the old elements
        elements = self.table

        # come up with a table size equal to the next prime number 2x larger than the current size
        newSize = self.tableSize * 2 + 1
        while (not self.isPrime(self.tableSize)):
            newSize += 2

        # set the hash table's table to a new table more than 2x the size
        self.tableSize = newSize
        self.table = MyHashTable(newSize)
        self.collisionCount = 0

        #transfer the elements over by rehashing them
        for listAtIndex in elements:
            for tuple in listAtIndex:
                #insert the newly hashed element into the new array
                self.insert(tuple[0], tuple[1])

    """
    this function takes a key and returns the item (key, item) pair from the hash table
    associated with the key. If no key-item pair is associated with the key, the function raises a
    LookupError exception.
    """
    def get(self, key):
            #for all items at each key, check
            for i in range(0, len(self.table[self.hash(key, self.tableSize)])):
                #set item to the tuple at the specified index and collision number
                item = self.table[self.hash(key, self.tableSize)][i]

                #if the item found isn't empty and has the desired key, return the item
                if (item != None and item[0] == key):
                    return item

            if (item is None):
                raise LookupError("Nothing was found in the table of elements at key \'" + str(key) + "\'")
            else:
                raise LookupError("There was no item found in the table of elements with the key \'" + str(key) + "\'")

    """
    this function takes a key, removes the key-item pair from the hash table and returns
    the key-item pair. If no key-item pair is associated with the key, the function raises a LookupError
    exception.
    """
    def remove(self, key):
        #preserve the first element at the key index and the collision number
        #for all items at each key, check
        for i in range(0, len(self.table[self.hash(key, self.tableSize)])):
            #set item to the tuple at the specified index and collision number
            removed = self.table[self.hash(key, self.tableSize)][i]

            #if the item found isn't empty and has the desired key, return the item
            if (removed != None and removed[0] == key):

                #decrement the collision and num_elements counters
                self.num_elements -= 1
                self.collisionCount -= 1
                return self.table[self.hash(key, self.tableSize)].pop(i)

        if (removed is None):
            raise LookupError("Nothing was found in the table of elements at key \'" + str(key) + "\'")

    """
    this function returns the number of key-item pairs currently stored in the hash table.
    """
    def size(self):
        return self.num_elements

    """
    this function returns the current load factor of the hash table.
    if it's over 50%, the table needs to be expanded
    """
    def loadFactor(self):
        return self.size()/(self.tableSize)

    """
    this function returns the number of collisions that have occurred during insertions into
    the hash table. A collision occurs when an item is inserted into the hash table at a location where one or
    more key-item pairs has already been inserted. When the table is resized, do not increment the number
    of collisions unless a collision occurs when the new key-item pair is being inserted into the resized hash
    table
    """
    def collisions(self):
        return self.collisionCount

    """
    hash the given value to get a key
    """
    def hash(self, value, primeNum):
        return value % primeNum

    def toString(self):
        output = "{\n"
        # run through all the elements in the table
        for i in range(len(self.table)):
            output += "["
            for element in self.table[i]:
                output += str(element) + ", "

            if output[-2: 0] == ", ":
                #lop off the last 2 characters to make the output a complete list
                output = output[0: -2]

            output += "]\n"
        output += "}"

        return output