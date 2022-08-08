class StackLinkedList:
    """Implements an efficient last-in first-out Abstract Data Type using a linked List"""

    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

        def __init__(self, item, next):
            # set stuff
            self.item = item
            self.next = next

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity  # Capacity of your stack
        self.head = None  # expect an instance of type Node - This is the starting point of the linked list
        self.num_items = 0  # number of elements in the stack


    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
        if (self.num_items == 0):
            return True
        else:
            return False

    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""
        if (self.capacity == self.num_items):
            return True
        else:
            return False

    def push(self, item):
        """Adds item to the stack"""
        #Make sure there's something being added and that there's still space
        if(item != None and self.capacity > self.num_items):
            self.num_items += 1
            self.head = StackLinkedList.Node(item, self.head)
        else:
            raise IndexError("Stack was full, item \'" + str(item) + "\' was not pushed.")

    def pop(self):
        """Returns the current top of the stack"""
        #Make sure there's something in the LinkedList
        if (self.is_empty()):
            raise IndexError("Couldn't remove anything from stack because stack was empty.")
        else:
            top = self.head.item
            self.num_items -= 1
            self.head = self.head.next
            return top

    def peek(self):
        """Returns the value of the item at the top of the stack without removing it"""
        #Make sure there's something in the LinkedList
        if(self.is_empty()):
            return None
        else:
            return self.head.item

    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        return self.num_items

    if (__name__ == "__main__"):
        print("This should not be showing")