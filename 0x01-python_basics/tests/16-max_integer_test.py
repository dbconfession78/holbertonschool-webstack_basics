#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("16-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    def test_int_in_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_bool_in_list(self):
        self.assertEqual(max_integer([True, False, -2]), 1)

    def test_float_in_list(self):
        self.assertEqual(max_integer([3.0, 2.0, 5.0]), 5.0)

    def test_large_number(self):
        num = 99999999999999999999999
        self.assertEqual(max_integer([num, 1]), 99999999999999999999999)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_no_input(self):
        self.assertIsNone(max_integer(), None)

    def test_neg_int_in_list(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_string(self):
        self.assertEqual(max_integer("Hello"), 'o')

    def test_tuple_in_list(self):
        self.assertEqual(max_integer([(2, 3)]), (2, 3))

    def test_tuple_as_list(self):
        self.assertEqual(max_integer((2, 3)), 3)

    def test_set_in_list(self):
        self.assertEqual(max_integer([{2, 3}, {3, 4}]), {2, 3})

    def test_max_in_middle(self):
        self.assertEqual(max_integer([2, 90, 4]), 90)


class ExpectedFailureCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_string_in_list(self):
        self.assertEqual(max_integer(["Hello", 2, 3, 4]), 4)

    @unittest.expectedFailure
    def test_undefined_var_in_list(self):
        self.assertEqual(max_integer([a, 2, 3, 4]), 4)

    @unittest.expectedFailure
    def test_none_as_list(self):
        self.assertEqual(max_integer(None), 1)

    @unittest.expectedFailure
    def test_int_as_list(self):
        self.assertEqual(max_integer(2), 2)

    @unittest.expectedFailure
    def test_float_as_list(self):
        self.assertEqual(max_integer(2.0), 2.0)

    @unittest.expectedFailure
    def test_none_in_list(self):
        self.assertEqual(max_integer([1, 2, None, 4]), 4)

    @unittest.expectedFailure
    def test_neg_sign_before_list(self):
        self.assertEqual(max_integer(-[1, 2, 3, 4]), 4)

    @unittest.expectedFailure
    def test_set_as_list(self):
        self.assertEqual(max_integer({2, 3}), 3)

    @unittest.expectedFailure
    def test_tuple_and_int_in_list(self):
        self.assertEqual(max_integer((2, 3), 9), 9)

    @unittest.expectedFailure
    def test_set_and_int_in_list(self):
        self.assertEqual(max_integer({2, 3}, 9), 9)

if __name__ == '__main__':
    unittest.main()
