import random

def swap(list, left, right):
    temp = list[left]
    list[left] = list[right]
    list[right] = temp

def subList(list, start, end=-1):
    sublist = []
    if (end >= 0):
        for i in range(start, end):
            sublist.append(list[i])
    else:
        for i in range(start, len(list)):
            sublist.append(list[i])

    return sublist

def indexOfMedOf3(list):
    # select 3 random elements
    medianElements = []
    medianElements.append(list[random.randint(0, len(list) - 1)])
    medianElements.append(list[random.randint(0, len(list) - 1)])
    medianElements.append(list[random.randint(0, len(list) - 1)])

    # sort the median element list
    #you should increment the comparisonCount vars by 2 every time this is run
    while (not isSorted(medianElements)):
        for i in range(1, 3):
            if (medianElements[i - 1] > medianElements[i]):
                swap(medianElements, i - 1, i)

    return list.index(medianElements[1])

def partitionHalf(list):
    # when the main list has been successfully partitioned
    # partition one half of the list
    # if there are no elements on this side
    if (list is None):
        list = []
        return 0
    # if there are less than 3 elements on this side, just use the index of the first element
    elif (len(list) < 3):
        return partition(list, 0) + 1
    # otherwise, use the median of 3
    else:
        return partition(list, indexOfMedOf3(list)) + 1

"""
When partition() completes it work (in linear time), the elements will have been rearranged such that the
pivot element is in the correct location, and all elements "less than" the pivot element are located at
indices less than that of the pivot index, and all elements "greater than" the pivot element are located
at indices greater than the pivot index. 

The version of the partition() method I wrote swaps the pivot element with the last element in the list,
swaps all elements so that those less than the pivot are to the left of those greater than the pivot,
and the pivot is at the end
This may add 1 to n inside the log(n) portion of the O(n) notation,
or slightly increase the time complexity, but it's how my professor wants it, so it is what it is
"""
def partition(list, pivotIndex):

    """
    #for debugging
    print("list being partitioned: " + str(list))
    print("pivot = " + str(list[pivotIndex]))
    """
    #termination condition
    #if the list is broken, empty, or sorted, return the comparison count
    if (list is None or list == [] or isSorted(list)):
        return 0

    pivot = list[pivotIndex]
    comparisonCount = 0

    #termination condition
    comparisonCount += 1
    if (len(list) < 3):
        #if there are only 2 elements in the list, put them in the right order
        comparisonCount += 1
        if (len(list) == 2):
            if (list[0] > list[1]):
                swap(list, 0, 1)
            return comparisonCount
        else:
            return comparisonCount

    #otherwise, if there are more than 2 elements in the list
    else:
        # swap the pivot with the last element
        partitionedList = list
        swap(partitionedList, pivotIndex, -1)

        # set start to the start of the partitioned list and end to 1 before the end (last element is the pivot)
        start = 0
        end = len(partitionedList) - 2

        # while the start is before the end index
        while (start < end):
            #if the element currently being read is greater than the pivot
            """
            #for debugging
            print("pivot = " + str(pivot))
            print("start = " + str(partitionedList[start]))
            print("end = " + str(partitionedList[end]))
            print("list before partitioning: " + str(partitionedList))
            """
            #if the current item being read is greater than or equal to the pivot
            comparisonCount += 1
            if (partitionedList[start] >= pivot):
                #if the element at the end of the list currently being read isn't where it should be
                comparisonCount += 1
                if (partitionedList[end] < pivot):
                    #swap it with the current element in the list being read
                    swap(partitionedList, start, end)

                #you can't do this, it's cheating
                #partitionedList.append(partitionedList.pop(start))
                #it automatically moves to the next element when it removes an element

                    start += 1

                #decrement the end index
                end -= 1

            #otherwise, if the current element is less than the pivot (ie where it should be)
            else:
                #move to the next element
                start += 1

        #get the partitioning location
        comparisonCount += 1
        if (partitionedList[start] >= pivot):
            partitionIndex = start
        else:
            partitionIndex = start + 1

        """
        #for debugging
        print("pivot = " + str(pivot))
        print("start = " + str(partitionedList[start]))
        print("end = " + str(partitionedList[end]))
        print("list after partitioning: " + str(partitionedList))
        """
        #when the main list has been successfully partitioned

        #partition the left half of the list from index 0
        #to the beginning of the set of elements greater than the original pivot
        #for debugging
        #print("partitioning left portion")
        left = subList(partitionedList, 0, partitionIndex)
        comparisonCount += partitionHalf(left)

        #partition the right half of the list from the beginning of the set of elements greater than the original pivot
        #to the end of the list
        #for debugging
        #print("partitioning right portion")
        right = subList(partitionedList, partitionIndex)
        comparisonCount += partitionHalf(right)

        #put both partitioned halves together and set list
        combinedList = left + right
        for i in range(len(list)):
            #for debugging
            #print(str(i))
            list[i] = combinedList[i]
        return comparisonCount

def quicksort(list, PIVOT_FIRST=True):
    #partition using the first element
    if (PIVOT_FIRST):
        #partition and swap stuff recursively
        return partition(list, 0)

    #partition using the median of 3
    else:
        #if there aren't enough elements to find indexOfedOf3
        if (len(list) < 3):
            # if there are only 2 elements in the list, put them in the right order
            if (len(list) == 2):
                if (list[0] > list[1]):
                    swap(list, 0, 1)
                return 3
            return 2

        # otherwise, if there are more than 2 elements in the list
        else:
            #partition and swap stuff recursively
            return partition(list, indexOfMedOf3(list)) + 1


def isSorted(list):
    #if every element in the list is greater than the previous one, return true
    #otherwise, if a single element is not in order, return false
    for i in range(1, len(list)):
        if (list[i-1] > list[i]):
            return False

    return True

def printf(list):
    string = "{\n"

    for i in range(len(list)):
        string += str(list[i]) + ", "

        #print elements in square-ish blocks
        if (i % (int)(len(list) ** 0.5) == 0):
            #remove the last 2 characters from the string being printed
            string = string[0: -2]
            string += "\n"

    string += "\n}"

    print(string)