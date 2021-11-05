import unittest
import quicksort
import math
import random

class MyTestCase(unittest.TestCase):
    def test_quicksort(self):
        #test efficiency when sorting various numbers of elements
        listSizes = [10]#, 200, 400, 800]

        #Ordered, ascending (pivot = first)
        for listSize in listSizes:
            totalComparisons = 0
            maxPredictedComparisonCount = listSize * math.log10(listSize)

            #tests each list 10 times and get the average
            for test in range(10):
                list = []

                for i in range(listSize):
                    list.insert(0, random.randint(0, listSize))

                #sort the list
                list = quicksort.quicksort(list, False)
                comparisonCount = list[0]

                #quicksort the ordered list using the first element as the pivot
                comparisonCount = quicksort.quicksort(list)
                print(str(comparisonCount))

                self.assertTrue(comparisonCount <= maxPredictedComparisonCount)
                quicksort.printf(list)
                self.assertTrue(quicksort.isSorted(list))

                totalComparisons += comparisonCount

            #show the average number of collisions for this size of list
            averageComparisonCount = totalComparisons // 10
            print("Quicksort made " + str(averageComparisonCount)
                  + " comparisons on the list of size n = " + str(listSize) + ".")


        #Ordered, ascending (pivot = median of 3)
        for listSize in listSizes:
            totalComparisons = 0
            maxPredictedComparisonCount = listSize * math.log10(listSize)

            # tests each list 10 times and get the average
            for test in range(10):
                list = []

                for i in range(listSize):
                    list.insert(0, random.randint(0, listSize))

                # sort the list
                quicksort.quicksort(list, False)

                # quicksort the ordered list using the median of 3 elements as the pivot
                comparisonCount = quicksort.quicksort(list, False)
                print(str(comparisonCount))

                self.assertTrue(comparisonCount <= maxPredictedComparisonCount)
                quicksort.printf(list)
                self.assertTrue(quicksort.isSorted(list))

                totalComparisons += comparisonCount

            # show the average number of collisions for this size of list
            averageComparisonCount = totalComparisons // 10
            print("Quicksort made " + str(averageComparisonCount)
                  + " comparisons on the list of size n = " + str(listSize) + ".")


        #Random (average 10 runs) (pivot = first)
        for listSize in listSizes:
            totalComparisons = 0
            maxPredictedComparisonCount = listSize * math.log10(listSize)

            # tests each list 10 times and get the average
            for test in range(10):
                list = []

                for i in range(listSize):
                    list.insert(0, random.randint(0, listSize))

                #quicksort using the first item in the list
                comparisonCount = quicksort.quicksort(list)
                print(str(comparisonCount))

                self.assertTrue(comparisonCount <= maxPredictedComparisonCount)
                quicksort.printf(list)
                self.assertTrue(quicksort.isSorted(list))

                totalComparisons += comparisonCount

            # show the average number of collisions for this size of list
            averageComparisonCount = totalComparisons // 10
            print("Quicksort made " + str(averageComparisonCount)
                  + " comparisons on the list of size n = " + str(listSize) + ".")


        #Random (average 10 runs) (pivot = median of 3)
        #test lists of various sizes
        for listSize in listSizes:
            totalComparisons = 0
            maxPredictedComparisonCount = listSize * math.log10(listSize)

            #tests each list 10 times and get the average
            for test in range(10):
                list = []

                for i in range(listSize):
                    list.insert(0, random.randint(0, listSize))

                #quicksort using the median of 3 items in the list
                comparisonCount = quicksort.quicksort(list, False)
                print(str(comparisonCount))

                self.assertTrue(comparisonCount <= maxPredictedComparisonCount)
                quicksort.printf(list)
                self.assertTrue(quicksort.isSorted(list))

                totalComparisons += comparisonCount

            #show the average number of collisions for this size of list
            averageComparisonCount = totalComparisons // 10
            print("Quicksort made " + str(averageComparisonCount)
                  + " comparisons on the list of size n = " + str(listSize) + ".")


            """
            Observed Big O() behavior, ordered with pivot = first :
            Observed Big O() behavior, ordered with pivot = median of 3 :
            Observed Big O() behavior, random with pivot = first :
            Observed Big O() behavior, random with pivot = median of 3 : 
            """

if __name__ == '__main__':
    unittest.main()
