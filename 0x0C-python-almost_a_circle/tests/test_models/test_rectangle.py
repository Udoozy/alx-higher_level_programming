#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys

class TestRectangle(unittest.TestCase):
    def test_rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual((r1.id), 4)
        
        r2 = Rectangle(2, 10)
        self.assertEqual((r2.id), 5)
        
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual((r3.id), 12)
        
        self.assertRaises(TypeError, Rectangle, 10, "2")
        
        self.assertRaises(ValueError, Rectangle, 10, -10)
        
        r4 = Rectangle(3, 2)
        self.assertEqual(r4.area(), 6)
        
        r5 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r5.area(), 56)
        
        r6 = Rectangle(3, 4)
        captured_output = StringIO()
        sys.stdout = captured_output
        r6.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), "###\n###\n###\n###\n")
        
        
        