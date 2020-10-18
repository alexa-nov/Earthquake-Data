import unittest
from expression_eval import *
from stack_array import *

class MyTest(unittest.TestCase):

    def test_postfix_eval(self):
        self.assertEqual(postfix_eval("3"), 3)
        self.assertEqual(postfix_eval("3.0 5.0 +"), 8.0)
        self.assertEqual(postfix_eval("9 6 -"), 3)
        self.assertEqual(postfix_eval("3 3 *"), 9)
        self.assertEqual(postfix_eval("5 1 2 + 4 ^ + 3 -"), 83)
        self.assertEqual(postfix_eval("3 4 + 2 * 7 /"), 2)
        self.assertEqual(postfix_eval("-3 5 *"), -15)
        self.assertRaises(PostfixFormatException, postfix_eval, "3 5 + a")
        self.assertRaises(PostfixFormatException, postfix_eval, "3 + /")
        self.assertRaises(PostfixFormatException, postfix_eval, "3 4 5 6 7 + /")

    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix("3"), "3")
        self.assertEqual(infix_to_postfix("-3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3.0"), "-3 4 2 * 1 5 - 2 3.0 ^ ^ / +")
        self.assertEqual(infix_to_postfix("4 * ( 5 - ( 7 + 2 ) )"), "4 5 7 2 + - *")
        self.assertEqual(infix_to_postfix("( ( 3 + 4 ) * 2 ) / 7"), "3 4 + 2 * 7 /")
        self.assertEqual(infix_to_postfix("( 5 + 7 ) * ( 6 - 2 )"), "5 7 + 6 2 - *")
        self.assertEqual(infix_to_postfix("( 4 + 2 ) + ( 3 * ( 5  - 1 ) )"), "4 2 + 3 5 1 - * +")
        self.assertEqual(infix_to_postfix("3 + 3 + 3"), "3 3 + 3 +")
        self.assertEqual(infix_to_postfix("3 * 3 + 3"), "3 3 * 3 +")
        self.assertEqual(infix_to_postfix("3 ^ 3 + 3"), "3 3 ^ 3 +")
        self.assertEqual(infix_to_postfix("4 * ( 5 + 2 + 1 )"), "4 5 2 + 1 + *")

    def test_prefix_to_postfix_1(self):
        self.assertEqual(infix_to_postfix("3"), "3")
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("+ - 4 3.0 -5"), "4 3.0 - -5 +")
        self.assertEqual(prefix_to_postfix("+ * 9 2 3"), "9 2 * 3 +")
        
if __name__ == '__main__':
    unittest.main()
