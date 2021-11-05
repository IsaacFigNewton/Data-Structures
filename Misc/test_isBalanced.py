import unittest
import stack_linked_list

class MyTestCase(unittest.TestCase):
    """
    Give long strings with
    many symbols of interest (not just 2-3 pairs). Here are some test cases – test each case several times for
    different values:
    a) balanced strings with no symbols of interest
    b) balanced strings with several pairs of symbols of interest
    c) unbalanced strings: there are opening symbols of interest that do not have closing
    counterparts; however, all paired symbols of interest are correctly arranged.
    d) unbalanced strings: there are closing symbols of interest that do not have opening
    counterparts; however, all paired symbols of interest are correctly arranged.
    e) unbalanced strings: all opening symbols have closing counterparts, but they are not correctly
    arranged.
    f) unbalanced strings: there are opening symbols of interest that do not have closing counterparts
    and some paired symbols of interest are NOT correctly arranged.
    g) unbalanced strings: there are closing symbols of interest that do not have opening counterparts
    and some paired symbols of interest are NOT correctly arranged.
    """
    def testA1(self):
        input = "Hello World"
        self.assertEqual(stack_linked_list.isBalanced(input), True)
    def testA2(self):
        input = "1 + 2 - 3 * 4 / 5^6 % 7"
        self.assertEqual(stack_linked_list.isBalanced(input), True)
    def testA3(self):
        input = "AZQWSXEDCRFVTGBYHNUJMIKOLPqazwsxedcrfvtgbyhnujmikolp;',./\`1234567890-=:\"<>?|~!@#$%^&*_+"
        self.assertEqual(stack_linked_list.isBalanced(input), True)
    def testA4(self):
        input = "%28%29%5B%5D%7B%7D"
        self.assertEqual(stack_linked_list.isBalanced(input), True)

    def testB1(self):
        input = "{(Hello)} World"
        self.assertEqual(stack_linked_list.isBalanced(input), True)
    def testB2(self):
        input = "Hello {(([World]))}"
        self.assertEqual(stack_linked_list.isBalanced(input), True)
    def testB3(self):
        input = "{[{(Hello)}] (([World]))}"
        self.assertEqual(stack_linked_list.isBalanced(input), True)
    def testB4(self):
        input = "{[([{(He{ll}o)}] (([W[or](l)d])))]}"
        self.assertEqual(stack_linked_list.isBalanced(input), True)

    def testC1(self):
        input = "({[Hello World"
        self.assertEqual(stack_linked_list.isBalanced(input), False)
    def testC2(self):
        input = "Hello ({[World"
        self.assertEqual(stack_linked_list.isBalanced(input), False)
    def testC3(self):
        input = "([{[Hello[( ({[World{"
        self.assertEqual(stack_linked_list.isBalanced(input), False)
    def testC4(self):
        input = "({[H{el(lo[({ ([Worl[d{["
        self.assertEqual(stack_linked_list.isBalanced(input), False)

    def testD1(self):
        input = "Hello]}) World"
        self.assertEqual(stack_linked_list.isBalanced(input), False)
    def testD2(self):
        input = "Hello World]})"
        self.assertEqual(stack_linked_list.isBalanced(input), False)
    def testD3(self):
        input = "]}Hello]}) )]World]})"
        self.assertEqual(stack_linked_list.isBalanced(input), False)
    def testD4(self):
        input = "]}He)l]lo]}) )]Wo}rl)d]})"
        self.assertEqual(stack_linked_list.isBalanced(input), False)

    def testE1(self):
        input = "({[Hello)}] ({[World})]"
        self.assertEqual(stack_linked_list.isBalanced(input), False)
    def testE2(self):
        input = "({{([Hello))}]{[}] ({[World})]}"
        self.assertEqual(stack_linked_list.isBalanced(input), False)
    def testE3(self):
        input = "({{([Hello))}]{{[}(] ({[)}]}({[World}))]}"
        self.assertEqual(stack_linked_list.isBalanced(input), False)
    def testE4(self):
        input = "({({([H[e{l(l}o])))}([]{{[}(] ({[)}]}({[W{o[r}]ld})))])]}"
        self.assertEqual(stack_linked_list.isBalanced(input), False)

    def testF1(self):
        input = "{[(({[Hello)}] ({[World})]"
        self.assertEqual(stack_linked_list.isBalanced(input), False)
    def testF2(self):
        input = "({{([Hello))}]{[}] ({[World})]}"
        self.assertEqual(stack_linked_list.isBalanced(input), False)
    def testF3(self):
        input = "((((((({{{[[({{([Hello))}]{{[}(](([{ ({[)}]}({[World}))]}"
        self.assertEqual(stack_linked_list.isBalanced(input), False)
    def testF4(self):
        input = "((((((({{{[}]))[({{([He)l}]lo))}]{{[}(](([{ ({[)}]}({[Wo)r)ld}))]}"
        self.assertEqual(stack_linked_list.isBalanced(input), False)

    def testG1(self):
        input = "({[Hello)}] ({[World})])]}"
        self.assertEqual(stack_linked_list.isBalanced(input), False)
    def testG2(self):
        input = "{(({[Hello)}])}) ([{[World})])]}]}"
        self.assertEqual(stack_linked_list.isBalanced(input), False)
    def testG3(self):
        input = "{(({[Hello)}])})}) )]([{[World})])]})}]}"
        self.assertEqual(stack_linked_list.isBalanced(input), False)
    def testG4(self):
        input = "{(({[H]}el)]lo)}])})}) )]([{[Wo)r}]l)d})])]})}]}"
        self.assertEqual(stack_linked_list.isBalanced(input), False)

if __name__ == '__main__':
    unittest.main()
