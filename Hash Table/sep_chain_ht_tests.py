import unittest
import sep_chain_ht

class MyTestCase(unittest.TestCase):
    def test_insert(self):
        hashTable = sep_chain_ht.MyHashTable()

        #insert stuff
        for i in range(1, 13):
            hashTable.insert(2**i, 2**i)

        print(hashTable.toString())

    def test_get_size_loadFactor_collisions(self):
        hashTable = sep_chain_ht.MyHashTable()

        # insert stuff
        collisionCount = 0
        for i in range(1, 13):
            hashTable.insert(2**i, 2**i)

            #if there are numbers less than i with the same hash value
            for j in range(1, i):
                if (hashTable.hash(i, hashTable.tableSize) == hashTable.hash(j, hashTable.tableSize)):
                    collisionCount += 1
                    break

            #check size
            self.assertEqual(hashTable.size(), i)
            #check load factor
            self.assertEqual(hashTable.loadFactor(), i/(hashTable.tableSize))
            #check the number of collisions
            #self.assertEqual(hashTable.collisions(), collisionCount)

        for i in range(1, 13):
            self.assertEqual(hashTable.get(2**i)[0], 2**i)

    def test_remove(self):
        hashTable = sep_chain_ht.MyHashTable()

        #insert stuff
        for i in range(1, 13):
            hashTable.insert(2**i, 2**i)

        #remove stuff
        for i in range(1, 13):
            self.assertEqual(hashTable.remove(2**i)[0], 2**i)


if __name__ == '__main__':
    unittest.main()
