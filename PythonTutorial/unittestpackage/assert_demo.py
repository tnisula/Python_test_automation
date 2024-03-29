"""
https://docs.python.org/3/library/unittest.html#unittest.TestCase
"""
import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        # self.assertFalse(a, "a is not false")
        # self.assertTrue(a, "a is not true")
        self.assertTrue(a, "a is not false")
        b = False
        # self.assertFalse(b, "b is not false")
        self.assertFalse(b, "b is not true")

    def test_assertEqual(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a, b, msg="'a' is not equal to 'b'")


if __name__ == '__main__':
    unittest.main(verbosity=2)