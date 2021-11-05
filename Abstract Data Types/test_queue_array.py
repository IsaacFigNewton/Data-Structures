import unittest
import queue_array

class MyTestCase(unittest.TestCase):
    def test_size(self):
        print("\nRunning " + str(self))

        queueArray = queue_array.QueueArray(5)
        self.assertEqual(queueArray.size(), 0)

    def test_isempty(self):
        print("\nRunning " + str(self))

        queueArray = queue_array.QueueArray(5)
        self.assertEqual(queueArray.is_empty(), True)

    def test_isfull(self):
        print("\nRunning " + str(self))

        queueArray = queue_array.QueueArray(5)
        self.assertEqual(queueArray.is_full(), False)

    def test_enqueue(self):
        print("\nRunning " + str(self))

        queueArray = queue_array.QueueArray(5)

        for i in range(1, 6):
            queueArray.enqueue(i)
            self.assertEqual(queueArray.size(), i)

        self.assertEqual(queueArray.size(), 5)
        self.assertEqual(queueArray.is_full(), True)

    def test_dequeue(self):
        print("\nRunning " + str(self))

        queueArray = queue_array.QueueArray(5)

        for i in range(1, 6):
            queueArray.enqueue(i)
            self.assertEqual(queueArray.size(), i)

        for i in range(1, 6):
            self.assertEqual(queueArray.dequeue(), i)
            self.assertEqual(queueArray.size(), 5-i)

        self.assertEqual(queueArray.is_empty(), True)

        #Test looparound
        print("\nTesting that the queue loops around")
        i = 1
        while (i < 9):
            queueArray.enqueue(i)
            i += 1
            queueArray.enqueue(i)
            queueArray.dequeue()
            i += 1


    """
    def test_pushIndexError(self):
        print("\nRunning " + str(self))
        queueArray = queue_array.QueueArray(5)

        for i in range(1, 7):
            queueArray.enqueue(i)

    def test_popIndexError(self):
        print("\nRunning " + str(self))
        queueArray = queue_array.QueueArray(5)

        for i in range(1, 7):
            queueArray.enqueue(i)
    """

    def test_peek(self):
        print("\nRunning " + str(self))

        queueArray = queue_array.QueueArray(5)

        for i in range(1, 6):
            queueArray.enqueue(i)

        self.assertEqual(queueArray.peek(), 1)
        queueArray.dequeue()
        self.assertEqual(queueArray.peek(), 2)

if __name__ == '__main__':
    MyTestCase.main()
