import unittest
from simplepythonapp import calc

class TestClass2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*#" * 30)
        print("Class 2 -> class level setUp")
        print("*#" * 30)

    def setUp(self):
        print("Class 2 -> setUp")

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two strings as one
        concatenated string
        """
        result = calc.add2('abc', 'def')
        self.assertEqual(result, 'abcdef')

    def test_add_string_and_integer(self):
        """
        Test the addition of a string and an integer returns them as one
        concatenated string (in which the integer is converted to a string)
        """
        result = calc.add2('abc', 3)
        self.assertEqual(result, 'abc3')

    def test_add_string_and_number(self):
        """
        Test the addition of a string and a float returns them as one
        concatenated string (in which the float is converted to a string)
        """
        result = calc.add2('abc', '5.5')
        self.assertEqual(result, 'abc5.5')

    def tearDown(self):
        print("Class 2 -> tearDown")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 30)
        print("Class 2 -> class level tearDown")
        print("*#" * 30)

if __name__ == '__main__':
    unittest.main(verbosity=2)