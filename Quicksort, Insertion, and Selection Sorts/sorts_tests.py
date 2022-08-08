import unittest
import random
import time
import sorts

class MyTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        print("Running test_insertion_sort")
        print()

        #test efficiency when sorting various numbers of elements
        listSizes = [1000, 2000, 4000, 8000, 16000, 32000]

        for listSize in listSizes:
            list = []
            maxPredictedComparisonCount = (listSize ** 2) * 3
            avgPredCompCount = (listSize) ** 2 // 4

            for i in range(listSize):
                list.insert(0, random.randint(0, listSize))

            completionTime = time.time()
            comparisonCount = sorts.insertion_sort(list)
            completionTime = time.time() - completionTime

            print("List size: " + str(listSize))
            print("Estimated comparison count: " + str(avgPredCompCount))
            print("Comparison count: " + str(comparisonCount))
            print("Completion time: " + str(completionTime))
            print()
            #sorts.printf(list)

            self.assertTrue(comparisonCount <= maxPredictedComparisonCount)
            self.assertTrue(sorts.isSorted(list))

        listSizesToEstimate = [10**5, 5 * 10**5, 10**6, 10**7]

        for listSize in listSizesToEstimate:
            avgPredCompCount = (listSize - 1) ** 2

            print("List size: " + str(listSize))
            print("Estimated comparison count: " + str(avgPredCompCount))

        print()

    def test_selection_sort(self):
        print("Running test_selection_sort")
        print()

        #test efficiency when sorting various numbers of elements
        listSizesToTest = [1000, 2000, 4000]#, 8000, 16000, 32000]

        for listSize in listSizesToTest:
            list = []
            maxPredictedComparisonCount = listSize ** 2 * 3
            avgPredCompCount = listSize ** 2

            for i in range(listSize):
                list.insert(0, random.randint(0, listSize))

            completionTime = time.time()
            comparisonCount = sorts.selection_sort(list)
            completionTime = time.time() - completionTime

            print("List size: " + str(listSize))
            print("Estimated comparison count: " + str(avgPredCompCount))
            print("Comparison count: " + str(comparisonCount))
            print("Completion time: " + str(completionTime))
            print()
            #sorts.printf(list)

            self.assertTrue(comparisonCount <= maxPredictedComparisonCount)
            self.assertTrue(sorts.isSorted(list))

        listSizesToEstimate = [10**5, 5 * 10**5, 10**6, 10**7]

        for listSize in listSizesToEstimate:
            avgPredCompCount = (listSize) ** 2 // 4

            print("List size: " + str(listSize))
            print("Estimated comparison count: " + str(avgPredCompCount))

        print()

if __name__ == '__main__':
    unittest.main()
