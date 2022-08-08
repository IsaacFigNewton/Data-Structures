class StackArray:
    """Implements an efficient last-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity  # Capacity of your stack
        self.items = [None] * capacity  # initializing the stack
        print("Empty stack: " + str(self.items))
        self.num_items = 0  # number of elements in the stack

    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
        if (self.num_items == 0):
            return True
        else:
            return False

    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""
        if (self.num_items == self.capacity):
            return True
        else:
            return False

    def push(self, item):
        """Adds item to the top of the stack"""
        if (0 == self.num_items):
            #If the array starts out empty, just set the first empty spot to the item
            self.items[0] = item
            self.num_items += 1
        #Make sure there's space in the stack for the item
        elif (0 < self.num_items and self.num_items < self.capacity):
            #Add the item to the front of the list (top of the stack)
            self.items.insert(0, item)
            #Remove the last item in the stack
            self.items.pop(self.capacity)
            self.num_items += 1
            """
            #old code
            tempArray = [None]*self.capacity
            tempArray[0] = item
            for i in range(self.capacity-2):
                tempArray[i+1] = self.items[i]
            self.num_items += 1

            #even older code
            i = self.num_items-1
            while (i > 0):
                self.items[i] = self.items[i-1]
            self.items[0] = item
            self.num_items += 1
            """
        elif (self.num_items < 0):
            print("Something is very wrong with the push method.")
        else:
            raise IndexError("Stack was full, item \'" + str(item) + "\' was not pushed.")

        print("Pushed array: " + str(self.items))

    def pop(self):
        """Returns the current top of the stack"""
        if (0 == self.num_items):
            raise IndexError("Couldn't remove anything from stack because stack was empty.")
        elif (0 < self.num_items):
            #Remove the item from the top of the stack
            top = self.items.pop(0)
            #Add an empty item to the bottom of the stack
            self.items.insert(self.capacity, None)
            self.num_items -= 1
            """
            tempArray = [None]*self.capacity
            tempArray[self.capacity] = None
            for i in range(self.capacity-2):
                tempArray[i] = self.items[i+1]
            self.num_items -= 1
            """

            print("Popped array: " + str(self.items))
            return top
        else:
            print("Something is very wrong with the pop method.")

        print("Popped array: " + str(self.items))

    def peek(self):
        """Returns the value of the item at the top of the stack without removing it"""
        return self.items[0]
    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        return self.num_items