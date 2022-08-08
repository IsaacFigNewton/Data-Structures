class QueueLinkedList:
    """Implements an efficient first-in first-out Abstract Data Type using a linked List"""

    class Node:
        def __init__(self, item):
            self.previous = None
            self.item = item
            self.next = None

        def __init__(self, previous, item, next):
            self.previous = previous
            self.item = item
            self.next = next

    def __init__(self, capacity):
        """Creates and empty queue with a capacity"""
        self.capacity = capacity  # Capacity of your queue
        self.head = QueueLinkedList.Node(None, None, None) # expect an instance of type Node - This is the starting point of the linked list
        self.back = QueueLinkedList.Node(None, None, None) # expect an instance of type Node - This is the ending point of the linked list
        self.num_items = 0  # number of elements in the queue

    def is_empty(self):
        """Returns true if the queue self is empty and false otherwise"""
        if (self.num_items == 0):
            return True
        else:
            return False

    def is_full(self):
        """Returns true if the queue self is full and false otherwise"""
        if (self.num_items == self.capacity):
            return True
        else:
            return False

    def enqueue(self, item):
        """Adds item to the back of the queue"""
        #Make sure there's something being added and that there's still space
        if (item != None and self.num_items == 0):
            #Problem here maybe
            newNode = QueueLinkedList.Node(self.back, item, None)
            self.back.next = newNode
            self.back = newNode
            self.head = QueueLinkedList.Node(None, item, self.back)
            self.num_items += 1

            #Debugging
            print("Enqueued list:")
            self.printList(self.head)
        elif(item != None and self.num_items < self.capacity):
            #Problem here?
            newNode = QueueLinkedList.Node(self.back, item, None)
            self.back.next = newNode
            self.back = newNode
            self.num_items += 1

            #Debugging
            print("Enqueued list:")
            self.printList(self.head)
        else:
            raise IndexError("Queue was full or nothing was supplied, item \'" + str(item) + "\' was not enqueued.")

    def dequeue(self):
        """Returns the current front of the queue"""

        #Make sure there's something in the LinkedList
        if (self.is_empty()):
            raise IndexError("Couldn't remove anything from stack because stack was empty.")
        else:
            #Remove and return the item at the front of the queue
            front = self.head.item
            print("Item to be dequeued: " + str(front))
            self.head = self.head.next
            if (self.head.next != None):
                print("Next item: " + str(self.head.next.item))
            self.num_items -= 1

            #Debugging
            print("Dequeued list:")
            self.printList(self.head)

            return front

    def peek(self):
        """Returns the value of the item at the front of the queue without removing it"""
        return self.head.item

    def size(self):
        """Returns the number of elements currently in the queue, not the capacity"""
        return self.num_items

    def printList(self, queue):
        """Prints the contents of the linked list, starting at head"""
        node = queue
        string = ""
        while (node.next != None):
            string += "[" + str(node.item) + "], "
            node = node.next

        print(string)