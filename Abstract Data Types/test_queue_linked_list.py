import unittest
import queue_linked_list

class MyTestCase(unittest.TestCase):
    def test_stack(self):
        print("\nRunning " + str(self))

        # Create the queue linked list object
        queue = queue_linked_list.QueueLinkedList(5)
        # check that it's empty
        self.assertEqual(queue.is_empty(), True)
        self.assertEqual(queue.size(), 0)
        self.assertEqual(queue.peek(), None)

    def test_size(self):
        print("Running " + str(self))

        # Create the queue linked list object
        queue = queue_linked_list.QueueLinkedList(5)
        self.assertEqual(queue.size(), 0)

    def test_isempty(self):
        print("\nRunning " + str(self))

        # Create the queue linked list object
        queue = queue_linked_list.QueueLinkedList(5)
        self.assertEqual(queue.is_empty(), True)

    def test_isfull(self):
        print("\nRunning " + str(self))

        # Create the queue linked list object
        queue = queue_linked_list.QueueLinkedList(5)
        self.assertEqual(queue.is_full(), False)

    def test_enqueue(self):
        print("\nRunning " + str(self))

        # Create the queue linked list object
        queue = queue_linked_list.QueueLinkedList(5)

        # add elements to the list (add 1 too many if you like to make sure it doesn't try to fill it pas the capacity)
        for i in range(1, 6):
            queue.enqueue(i)
        # check the size of the list
        self.assertEqual(queue.is_full(), True)
        self.assertEqual(queue.size(), 5)
        # check that the element at the front is the first element that was added
        self.assertEqual(queue.peek(), 1)

    def test_dequeue(self):
        print("\nRunning " + str(self))

        # Create the queue linked list object
        queue = queue_linked_list.QueueLinkedList(5)

        # Add elements to the list
        for i in range(1, 6):
            queue.enqueue(i)

        # check that dequeueing works
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.dequeue(), 2)

        # remove elements
        for i in range(1, 3):
            queue.dequeue()

        # check that it's empty
        assert(queue.is_empty())
        self.assertEqual(queue.size(), 0)

    def test_peek(self):
        print("\nRunning " + str(self))

        # Create the queue linked list object
        queue = queue_linked_list.QueueLinkedList(5)

        # Add elements to the list
        for i in range(1, 6):
            queue.enqueue(i)

        # test that peeking works
        self.assertEqual(queue.peek(), 1)

if __name__ == '__main__':
    unittest.main()
