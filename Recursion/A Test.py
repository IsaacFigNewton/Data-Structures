import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(indexOf('Mississippi', "Miss"), 0)  #assert that "Miss" is at index 0 in "Mississippi"
        self.assertEqual(indexOf('Mississippi', "sip"), 6)  #assert that "sip" is at index 6 in "Mississippi"
        self.assertEqual(indexOf('Mississippi', "pi"), 9)  #assert that "pi" is at index 9 in "Mississippi"
        self.assertEqual(indexOf('Mississippi', "."), -1)  #assert that "." is at index -1 in "Mississippi"

if __name__ == '__main__':
    unittest.main()
