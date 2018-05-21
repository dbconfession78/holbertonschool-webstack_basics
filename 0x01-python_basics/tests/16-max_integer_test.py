#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('16-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class definition for TestMaxInteger
    """
    def test_tgt_in_list(self):
        """
        test case: target exists in list
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_float_in_list(self):
        """
        test case: float in list
        """
        self.assertEqual(max_integer([1.0, -1, -2, -3]), 1)

    def test_bool_in_list(self):
        """
        test case: boolean in list
        """
        self.assertEqual(max_integer([True, -1, -2, -3]), 1)

    def test_empty_list(self):
        """
        test case: input as None
        """
        self.assertEqual(max_integer([]), None)

    def test_has_negative_int(self):
        """
        test case: list contains negative int
        """
        self.assertEqual(max_integer([-3, -4, -5]), -3)

    def test_large_intt(self):
        """
        test case: large int in list
        """
        self.assertEqual(max_integer([99999999999999999999999, 1]),
                         99999999999999999999999)

    def test_input_as_none(self):
        """
        test case: input as None
        """
        self.assertIsNone(max_integer(), None)

    def test_input_as_string(self):
        """
        test case: input as a string
        """
        self.assertEqual(max_integer("Hello"), "o")

    def test_input_as_tuple(self):
        """
        test case: input as a tuple
        """
        self.assertEqual(max_integer((-3, -4, -5)), -3)

    def test_set_in_list(self):
        """
        test case: set in list
        """
        self.assertEqual(max_integer([{1, 2}, {3, 4}]), {1, 2})


class ExpectedFailureCase(unittest.TestCase):
    """
    Class: ExpectedFailureCase definition
    """

    @unittest.expectedFailure
    def test_string_in_list(self):
        """
        error case: list contains a string among ints
        """
        self.assertEqual(max_integer([1, 2, "3", 4, 5]), 4)

    @unittest.expectedFailure
    def test_undefined_var_in_list(self):
        """
        error case: list contains an undefined variable
        """
        self.assertEqual(max_integer([a, 2, 3, 4, 5]), 4)

    @unittest.expectedFailure
    def test_int_as_input(self):
        """
        error case: input as int
        """
        self.assertEqual(max_integer(2), 4)

    @unittest.expectedFailure
    def test_None_in_list(self):
        """
        error case: list contains None
        """
        self.assertEqual(max_integer([None, 2, "3", 4, 5]), 4)

    @unittest.expectedFailure
    def test_input_as_float(self):
        """
        error case: input as float
        """
        self.assertEqual(max_integer(4.0), 4)

    @unittest.expectedFailure
    def test_None_as_input(self):
        """
        error case: None as input
        """
        self.assertEqual(max_integer(None), 4)

    @unittest.expectedFailure
    def test_neg_sign_outside_list(self):
        """
        error case: list contains a string among ints
        """
        self.assertEqual(max_integer(-[1, 2, 3, 4, 5]), 5)

    @unittest.expectedFailure
    def test_set_as_input(self):
        """
        error case: set as input
        """
        self.assertEqual(max_integer({1, 2, 3}), 4)

    @unittest.expectedFailure
    def test_tuple_int_in_list(self):
        """
        error case: list contains ints and tuples
        """
        self.assertEqual(max_integer([(1, 2), 3, 4, 5]))

    @unittest.expectedFailure
    def test_set_int_in_list(self):
        """
        error case: sets and ints in list
        """
        self.assertEqual(max_integer([{1, 2}, 1, 2, 4, 5]), 5)


if __name__ == "__main__":
    unittest.main()
