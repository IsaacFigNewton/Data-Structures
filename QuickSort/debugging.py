import quicksort
import random

def modifyingList(list):
    list.append(1)
    list[0] = 69
    #list = [1, 2, 3]
    quicksort.swap(list, 0, 2)

    for i in range(len(list)):
        list[i] = 5
    """
    for i in range(len(list)):
        list[i] = alist[i]

    temp = list[0]
    list[0] = list[2]
    list[2] = temp
    """

    return "blue"

def indexOfMedOf3(list):
    # select 3 random elements
    medianElements = []
    medianElements.append(list[random.randint(0, len(list) - 1)])
    medianElements.append(list[random.randint(0, len(list) - 1)])
    medianElements.append(list[random.randint(0, len(list) - 1)])

    # sort the median element list
    #you should increment the comparisonCount vars by 2 every time this is run
    while (not quicksort.isSorted(medianElements)):
        for i in range(1, 3):
            if (medianElements[i - 1] > medianElements[i]):
                quicksort.swap(medianElements, i - 1, i)

    return list.index(medianElements[1])

"""
listSize = 10

list = []

for i in range(listSize):
    list.insert(0, random.randint(0, listSize))

print(list)
print(bub(list))
print(list)
#quicksort.printf(quicksort.quicksort(list))
"""

"""
list = []

for i in range(10):
    list.insert(0, random.randint(0, 10))

#sort the list
comparisonCount = quicksort.quicksort(list, False)

#quicksort the ordered list using the first element as the pivot
comparisonCount = quicksort.quicksort(list)
print(str(comparisonCount))
print(str(list))
"""
list = []
for i in range(10):
    list.insert(0, random.randint(0, 100))
print(list[indexOfMedOf3(list)])