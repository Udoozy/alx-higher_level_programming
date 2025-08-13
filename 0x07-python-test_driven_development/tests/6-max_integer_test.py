#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class for testing the max integer
    """
    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 0, 5, -2, 3]), 5)

    def test_repeated_numbers(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_max_at_start(self):
        self.assertEqual(max_integer([9, 5, 4, 1]), 9)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 7, 3, 2]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_all_equal_numbers(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.5]), 2.7)

    def test_negative_floats(self):
        self.assertEqual(max_integer([-2.5, -7.1, -1.2]), -1.2)

    def test_mixed_int_and_float(self):
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_zero_as_max(self):
        self.assertEqual(max_integer([-3, -1, 0]), 0)

if __name__ == '__main__':
    unittest.main()
