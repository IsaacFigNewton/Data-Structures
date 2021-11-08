import unittest
import quicksort
import math
import random

class MyTestCase(unittest.TestCase):
    def test_quicksort(self):
        #test efficiency when sorting various numbers of elements
        listSizes = [100, 200, 400, 800]


        print("Testing Ordered, ascending (pivot = first)")
        #Ordered, ascending (pivot = first)
        for listSize in listSizes:
            totalComparisons = 0
            maxPredictedComparisonCount = listSize * math.log2(listSize)

            #tests each list 10 times and get the average
            for test in range(10):
                list = []

                for i in range(listSize):
                    list.insert(0, random.randint(0, listSize))

                quicksort.printf(list)
                #sort the list
                comparisonCount = quicksort.quicksort(list, False)

                #quicksort the ordered list using the first element as the pivot
                comparisonCount = quicksort.quicksort(list)
                print(str(comparisonCount))
                quicksort.printf(list)
                print("")

                self.assertTrue(comparisonCount <= maxPredictedComparisonCount)
                quicksort.printf(list)
                self.assertTrue(quicksort.isSorted(list))

                totalComparisons += comparisonCount

            #show the average number of collisions for this size of list
            averageComparisonCount = totalComparisons // 10
            print("Quicksort made an average of " + str(averageComparisonCount)
                  + " comparisons on the list of size n = " + str(listSize) + ".")

        print("")

        print("Testing Ordered, ascending (pivot = median of 3)")
        #Ordered, ascending (pivot = median of 3)
        for listSize in listSizes:
            totalComparisons = 0
            maxPredictedComparisonCount = listSize * math.log2(listSize)

            # tests each list 10 times and get the average
            for test in range(10):
                list = []

                for i in range(listSize):
                    list.insert(0, random.randint(0, listSize))

                # sort the list
                quicksort.quicksort(list, False)

                # quicksort the ordered list using the median of 3 elements as the pivot
                quicksort.printf(list)
                comparisonCount = quicksort.quicksort(list, False)
                print(str(comparisonCount))
                quicksort.printf(list)
                print("")

                self.assertTrue(comparisonCount <= maxPredictedComparisonCount)
                #quicksort.printf(list)
                self.assertTrue(quicksort.isSorted(list))

                totalComparisons += comparisonCount

            # show the average number of collisions for this size of list
            averageComparisonCount = totalComparisons // 10
            print("Quicksort made an average of " + str(averageComparisonCount)
                  + " comparisons on the list of size n = " + str(listSize) + ".")

        print("")

        print("Testing Random (average 10 runs) (pivot = first)")
        #Random (average 10 runs) (pivot = first)
        for listSize in listSizes:
            totalComparisons = 0
            maxPredictedComparisonCount = listSize * listSize

            # tests each list 10 times and get the average
            for test in range(10):
                list = []

                for i in range(listSize):
                    list.insert(0, random.randint(0, listSize))

                #quicksort using the first item in the list
                quicksort.printf(list)
                comparisonCount = quicksort.quicksort(list)
                print(str(comparisonCount))
                quicksort.printf(list)
                print("")

                self.assertTrue(comparisonCount <= maxPredictedComparisonCount)
                #quicksort.printf(list)
                self.assertTrue(quicksort.isSorted(list))

                totalComparisons += comparisonCount

            # show the average number of collisions for this size of list
            averageComparisonCount = totalComparisons // 10
            print("Quicksort made an average of " + str(averageComparisonCount)
                  + " comparisons on the list of size n = " + str(listSize) + ".")

        print("")

        print("Testing Random (average 10 runs) (pivot = median of 3)")
        #Random (average 10 runs) (pivot = median of 3)
        #test lists of various sizes
        for listSize in listSizes:
            totalComparisons = 0
            maxPredictedComparisonCount = listSize * listSize

            #tests each list 10 times and get the average
            for test in range(10):
                list = []

                for i in range(listSize):
                    list.insert(0, random.randint(0, listSize))

                #quicksort using the median of 3 items in the list
                quicksort.printf(list)
                comparisonCount = quicksort.quicksort(list, False)
                print(str(comparisonCount))
                quicksort.printf(list)
                print("")

                self.assertTrue(comparisonCount <= maxPredictedComparisonCount)
                #quicksort.printf(list)
                self.assertTrue(quicksort.isSorted(list))

                totalComparisons += comparisonCount

            #show the average number of collisions for this size of list
            averageComparisonCount = totalComparisons // 10
            print("Quicksort made an average of " + str(averageComparisonCount)
                  + " comparisons on the list of size n = " + str(listSize) + ".")

if __name__ == '__main__':
    unittest.main()
