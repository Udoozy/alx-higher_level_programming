#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class testMaxInteger(unittest.TestCase):
    """Class for testing the max integer
    """
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -3, -5, 0]), 0)
        self.assertEqual(max_integer([]), None)
        
        with self.assertRaises(TypeError):
            max_integer([1, 2, '4'])