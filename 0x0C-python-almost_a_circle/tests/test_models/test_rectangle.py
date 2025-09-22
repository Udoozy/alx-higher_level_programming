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
        
        r7 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r7), "[Rectangle] (12) 2/1 - 4/6")
        
        r7 = Rectangle(4, 6, 2, 1)
        self.assertEqual(str(r7), "[Rectangle] (8) 2/1 - 4/6")
        
        r8 = Rectangle(4, 3, 2, 1)
        captured_output = StringIO()
        sys.stdout = captured_output
        r8.display()
        sys.stdout = sys.__stdout__
        expected_output = "\n  ####\n  ####\n  ####\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
        
        r9 = Rectangle(10, 20, 1, 2, 99)
        self.assertEqual((r9.id, r9.width, r9.height, r9.x, r9.y), (99, 10, 20, 1, 2))
        r9.update(42, 7, 14, 3, 5)
        self.assertEqual(r9.id, 42)
        self.assertEqual(r9.width, 7)
        self.assertEqual(r9.height, 14)
        self.assertEqual(r9.x, 3)
        self.assertEqual(r9.y, 5)
