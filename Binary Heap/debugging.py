import bin_heap

def debug(self, rootIndex, insertedElementIndex):
    # precipitate up (self is elements array)
    # don't forget that 2 * (i+1) - 1 is the index of the left child and 2 * (i+1) is the index of the right child
    # (where i is the index of the parent node's value in the array and we're doing i-1 because the array's starting at 0)

    # while the inserted element hasn't been precipitated to the correct location or the root node hasn't been swapped
    while (insertedElementIndex != rootIndex):
        print(self.elements)
        insertedElement = self.elements[insertedElementIndex]

        # determine whether the insertedNode is the left or right child
        # and set the parentNode index appropriately
        if (insertedElementIndex % 2):
            parentElementIndex = insertedElementIndex // 2 - 1
        else:
            parentElementIndex = (insertedElementIndex + 1) // 2 - 1

        # determine the parentElement's value
        parentElement = self.elements[parentElementIndex]

        tempElement = parentElement
        # if the new insertion is less than the parent element, swap them
        if (insertedElement < parentElement):
            self.elements[parentElementIndex] = self.elements[insertedElementIndex]
            self.elements[insertedElementIndex] = tempElement

            # update the insertedElementIndex to the element's current location in the heap/tree
            insertedElementIndex = parentElementIndex
        # otherwise, just break, the element has been precipitated to the correct location
        else:
            break

if __name__ == "__main__":
    self = bin_heap.BinHeap(7)

    self.elements[0] = 5

    self.elements[1] = 6
    self.elements[2] = 8

    self.elements[3] = 7
    self.elements[4] = 9
    self.elements[5] = 2
    self.elements[6] = 22

    print(self.elements)

    debug(self, 0, 5)