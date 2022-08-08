import unittest
import stack_linked_list
"""
import sys
sys.path.append('C:\\Users\\igeek\\PycharmProjects\\Lab 2 - Linked List Implementation\\venv')
from stacked_linked_list.py import StackedLinkedList
"""

class MyTestCase(unittest.TestCase):
    def test_stack(self):
        print("\nRunning " + str(self))

        #Create the stacked linked list object
        list = stack_linked_list.StackLinkedList(5)
        #check that it's empty
        assert(list.is_empty() == True)
        assert(list.size() == 0)
        assert(list.peek() == None)

    def test_size(self):
        print("Running " + str(self))

        #Create the stacked linked list object
        list = stack_linked_list.StackLinkedList(5)
        self.assertEqual(list.size(), 0)

    def test_isempty(self):
        print("\nRunning " + str(self))

        #Create the stacked linked list object
        list = stack_linked_list.StackLinkedList(5)
        self.assertEqual(list.is_empty(), True)

    def test_isfull(self):
        print("\nRunning " + str(self))

        #Create the stacked linked list object
        list = stack_linked_list.StackLinkedList(5)
        self.assertEqual(list.is_full(), False)

    def test_push(self):
        print("\nRunning " + str(self))

        #Create the stacked linked list object
        list = stack_linked_list.StackLinkedList(5)

        #add elements to the list (add 1 too many if you like to make sure it doesn't try to fill it pas the capacity)
        for i in range(1,6):
            list.push(i)
        #check the size of the list
        assert(list.is_full() == True)
        assert(list.size() == 5)
        #check that the element on top is the last element that was added
        assert(list.peek() == i)

    def test_pop(self):
        print("\nRunning " + str(self))

        # Create the stacked linked list object
        list = stack_linked_list.StackLinkedList(5)

        #Add elements to the list
        for i in range(1, 6):
            list.push(i)

        #check that popping works
        assert(list.pop() == 5)
        assert(list.size() == 4)
        assert(list.peek() == 4)
        #remove elements
        for i in range(1,5):
            list.pop()
        #check that it's empty
        assert(list.is_empty() == True)
        assert(list.size() == 0)

    def test_peek(self):
        print("\nRunning " + str(self))

        # Create the stacked linked list object
        list = stack_linked_list.StackLinkedList(5)

        # Add elements to the list
        for i in range(1, 6):
            list.push(i)

        #test that peeking works
        assert(list.peek() == 5)

if __name__ == '__main__':
    unittest.main()