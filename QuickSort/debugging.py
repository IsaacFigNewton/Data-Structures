import quicksort
import random

def bub(list):
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

listSize = 10

list = []

for i in range(listSize):
    list.insert(0, random.randint(0, listSize))

print(list)
print(bub(list))
print(list)
#quicksort.printf(quicksort.quicksort(list))