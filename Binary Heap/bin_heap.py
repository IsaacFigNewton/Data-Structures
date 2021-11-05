class BinHeap:
    class MyException(Exception):
        def __init__(self, message):
            self.message = message

    def __init__(self, capacity):
        #+1 because it starts at i=1 instead of i=0
        self.elements = [None] * (capacity + 1)
        self.num_elements = 0
        self.capacity = capacity

    def getElementIndex(self, value):
        return self.elements.index(value)

    def getSmallChildIndex(self, mainIndex):
        #if the mainIndex is on the edge of what is allowable
        #if the left child wouldn't fit in the tree
        if (mainIndex * 2 > self.capacity):
            return

        #if the left child would fit but the right child wouldn't
        elif (mainIndex * 2 == self.capacity and mainIndex * 2 + 1 > self.capacity):
            #return the left child, regardless of its value
            return mainIndex * 2

        #otherwise, if there are 2 valid child indices:
        else:
            leftChild = self.elements[mainIndex * 2]
            rightChild = self.elements[mainIndex * 2 + 1]

            # if the left or right child has a value
            if (leftChild != None or rightChild != None):
                #if the left child is the only one with a value
                if (leftChild != None and rightChild is None):
                    return mainIndex * 2
                #if the right child is the only one with a value
                elif (leftChild is None and rightChild != None):
                    return mainIndex * 2 + 1
                #otherwise, both children must have values, so get the smallest
                elif (leftChild < rightChild):
                    return mainIndex * 2
                else:
                    return mainIndex * 2 + 1
            #otherwise, if there are no children, just return None
            else:
                return

    def precipitateUp(self, rootIndex, insertedElementIndex):
        # precipitate up (self is elements array)
        # don't forget that 2 * iis the index of the left child and 2 * i + 1 is the index of the right child
        # (where i is the index of the parent node's value in the array and we're doing i-1 because the array's starting at 0)

        #while the inserted element hasn't been precipitated to the correct location or the root node hasn't been swapped
        while (insertedElementIndex != rootIndex):
            insertedElement = self.elements[insertedElementIndex]

            #determine whether the insertedNode is the left or right child
            #and set the parentNode index appropriately
            parentElementIndex = insertedElementIndex // 2

            #determine the parentElement's value
            parentElement = self.elements[parentElementIndex]

            tempElement = parentElement
            #if the new insertion is less than the parent element, swap them
            if (insertedElement < parentElement):
                self.elements[parentElementIndex] = self.elements[insertedElementIndex]
                self.elements[insertedElementIndex] = tempElement

                #update the insertedElementIndex to the element's current location in the heap/tree
                insertedElementIndex = parentElementIndex
            #otherwise, just break, the element has been precipitated to the correct location
            else:
                break

    def insert(self, element):
        #check to make sure there's space for another element
        #if there's space for more elements in an array, add the element after all the others
        if (self.num_elements == 0):
            self.elements[1] = element
            #precipitate up
            self.precipitateUp(1, 1)

        elif (self.num_elements < self.capacity):
            self.elements[self.num_elements + 1] = element
            #precipitate up
            self.precipitateUp(1, self.num_elements + 1)

        #otherwise, if there's no space left, double the size of the array of elements
        else:
            print("Expanding the list")
            #create a new array 2x the size of the original
            newArray = [None] * 2 * (self.capacity + 1)

            #put the elements in it in the same places as they were in the old array
            for i in range(1, self.num_elements + 1):
                newArray[i] = self.elements[i]

            #add the new element
            newArray[self.num_elements + 1] = element

            #set it as the main array
            self.elements = newArray
            # precipitate the new element
            self.precipitateUp(1, self.num_elements + 1)

        self.num_elements += 1
        print("Added \'" + str(element) + "\' to array.")
        print("self.elements = " + str(self.elements))

    def deleteMin(self):
        if (self.isEmpty()):
            raise BinHeap.MyException("Couldn't remove element from heap because heap was empty.")

        removedElement = self.elements[1]

        #set the root to the smaller child's value
        smallChildIndex = self.getSmallChildIndex(1)

        # if the minimum element doesn't have any children
        if (smallChildIndex is None):
            self.elements[1] = None
        #if it has children
        else:
            self.elements[1] = self.elements[smallChildIndex]
            #determine what side to shift elements and remove the bottom-most node from
            #instantiate the index counter
            indexOfNextElementToShift = smallChildIndex
            indexOfCurrentElement = smallChildIndex

            #while there is a child for the current element
            #and the index of the right child is within the bounds of the array
            while (True):
                #save the index of the current element
                indexOfCurrentElement = indexOfNextElementToShift
                #get the index of the child to move into this element's place
                indexOfNextElementToShift = self.getSmallChildIndex(indexOfCurrentElement)
                #if a child is found, shift it into the place of the current element
                if (indexOfNextElementToShift != None):
                    #shift the child element into the current element's place
                    self.elements[indexOfCurrentElement] = self.elements[indexOfNextElementToShift]
                #otherwise, set the current element to None (it becomes a leaf)
                else:
                    self.elements[indexOfCurrentElement] = None
                    break

        self.num_elements -= 1

        print("Removed \'" + str(removedElement) + "\' from array.")
        print("self.elements = " + str(self.elements))
        return removedElement

    def isEmpty(self):
        if (self.num_elements == 0):
            return True
        else:
            return False

    def size(self):
        #return the number of elements in the collection, not the array
        return self.num_elements

    def __string__(self):
        #format the string of (non-None) elements to return nicely
        string = "{"
        for element in self.elements:
            if (element != None):
                string += str(element) + ", "

        #remove the last 2 characters ", "
        string = string[0:-2]

        string += "}"

        return string

