#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual((r1.id), 4)
        
        r2 = Rectangle(2, 10)
        self.assertEqual((r2.id), 5)
        
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual((r3.id), 12)
