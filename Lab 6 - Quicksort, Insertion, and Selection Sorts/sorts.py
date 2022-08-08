def swap(alist, left, right):
    list = alist

    temp = list[left]
    list[left] = list[right]
    list[right] = temp

    #return swapped list
    return list

def minimumIndex(list):
    currentMinIndex = 0

    for i in range(len(list)):
        if (list[i] < list[currentMinIndex]):
            currentMinIndex = i

    return currentMinIndex

def subList(list, start):
    sublist = []
    for i in range(start, len(list)):
        sublist.append(list[i])

    return sublist

def insertion_sort(alist):
    comparisonCount = 0

    for i in range(1, len(alist)):
        j = i

        #while the previous and current elements are out of order
        while (j >= 1 and alist[j - 1] > alist[j]):
            #swap the elements and take a step further down the list
            alist = swap(alist, j - 1, j)
            j -= 1

            #increment the comparison counter
            comparisonCount += 1

    #return the number of comparisons
    return comparisonCount

def selection_sort(alist):
    comparisonCount = 0

    #for every item in the list
    for i in range(len(alist)):
        remainingList = subList(alist, i)

        #compensate for not being able to figure out how to count the elements in subList above
        comparisonCount += len(alist) - i

        #find the minimum in the remainder of the unsorted list
        #swap the current element being analyzed and the smallest element found in the rest of the list
        alist = swap(alist, i, i + minimumIndex(remainingList))

        #compensate for not being able to figure out how to count the elements in minimumIndex above
        comparisonCount += len(remainingList)

        #increment the comparison counter
        comparisonCount += 1

    #return the number of comparisons
    return comparisonCount

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