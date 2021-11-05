class QueueArray:
    """Implements an efficient first-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates an empty queue with a capacity"""
        self.capacity = capacity  # Capacity of your queue
        self.items = [None] * capacity  # initializing the queue
        self.num_items = 0  # number of elements in the queue
        self.start = 0
        self.end = 0

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
        """Adds item to the queue"""
        if (0 > self.num_items):
            print("Something is very wrong with the enqueue method.")
        elif (0 == self.num_items):
            self.items[self.end] = item

            if (self.end + 1 > self.capacity):
                raise IndexError("Somehow the \'end\' index marker got mangled.")
            elif (self.end + 1 == self.capacity):
                self.end = 0
            else:
                self.end += 1

            # Increment the num_items value
            self.num_items += 1

            print("Enqueued array: " + str(self.items))
        elif (0 < self.num_items and self.num_items < self.capacity):
            self.items[self.end] = item

            if (self.end + 1 > self.capacity):
                raise IndexError("Somehow the \'end\' index marker got mangled.")
            elif (self.end + 1 == self.capacity):
                self.end = 0
            else:
                self.end += 1

            # Increment the num_items value
            self.num_items += 1

            print("Enqueued array: " + str(self.items))
        else:
            raise IndexError("Queue was full, item \'" + str(item) + "\' was not enqueued.")

    def dequeue(self):
        """Returns the current front of the queue"""
        if (0 > self.num_items):
            print("Something is very wrong with the dequeue method.")
        elif (0 == self.num_items):
            raise IndexError("Queue was empty,nothing was dequeued.")
        elif (0 < self.num_items and self.num_items <= self.capacity):
            # Dequeue the item at the front of the queue and replace it with an empty item
            front = self.items.pop(self.start)
            self.items.insert(self.start, None)
            """
            if (self.end + 1 > self.capacity):
                raise IndexError("Somehow the \'end\' index marker got mangled.")
            elif (self.end + 1 == self.capacity):
                self.items.insert(0, None)
            else:
                self.items.insert(self.end + 1, None)
            """
            #Shift the start pointer
            if (self.start + 1 > self.capacity):
                raise IndexError("Somehow the \'start\' index marker got mangled.")
            elif (self.start + 1 == self.capacity):
                self.start = 0
            else:
                self.start += 1

            # Decrement the num_items value
            self.num_items -= 1

            print("Dequeued array: " + str(self.items))
            return front

    def peek(self):
        """Returns the value of the item at the front of the queue without removing it"""
        return self.items[self.start]

    def size(self):
        """Returns the number of elements currently in the queue, not the capacity"""
        return self.num_items