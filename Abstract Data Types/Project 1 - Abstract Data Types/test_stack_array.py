import unittest
import stack_array

class MyTestCase(unittest.TestCase):
    def test_size(self):
        print("Running " + str(self))

        stackArray = stack_array.StackArray(5)
        self.assertEqual(stackArray.size(), 0)

    def test_isempty(self):
        print("\nRunning " + str(self))

        stackArray = stack_array.StackArray(5)
        self.assertEqual(stackArray.is_empty(), True)

    def test_isfull(self):
        print("\nRunning " + str(self))

        stackArray = stack_array.StackArray(5)
        self.assertEqual(stackArray.is_full(), False)

    def test_push(self):
        print("\nRunning " + str(self))

        stackArray = stack_array.StackArray(5)

        for i in range(1, 6):
            stackArray.push(i)
            self.assertEqual(stackArray.size(), i)

        self.assertEqual(stackArray.size(), 5)
        self.assertEqual(stackArray.is_full(), True)

    def test_pop(self):
        print("\nRunning " + str(self))

        stackArray = stack_array.StackArray(5)

        for i in range(1, 6):
            stackArray.push(i)

        for i in range(1, 6):
            self.assertEqual(stackArray.pop(), 6-i)
        self.assertEqual(stackArray.size(), 0)
        self.assertEqual(stackArray.is_empty(), True)

    """
    def test_pushIndexError(self):
        print("\nRunning " + str(self))
        stackArray = stack_array.StackArray(5)

        for i in range(1, 7):
            stackArray.push(i)

    def test_popIndexError(self):
        print("\nRunning " + str(self))
        stackArray = stack_array.StackArray(5)

        for i in range(1, 6):
            stackArray.push(i)

        for i in range(1, 7):
            self.assertEqual(stackArray.pop(), 6 - i)
    """

    def test_peek(self):
        print("\nRunning " + str(self))

        stackArray = stack_array.StackArray(5)

        for i in range(1, 6):
            stackArray.push(i)

        self.assertEqual(stackArray.peek(), 5)
        stackArray.pop()
        self.assertEqual(stackArray.peek(), 4)

if __name__ == '__main__':
    unittest.main()
