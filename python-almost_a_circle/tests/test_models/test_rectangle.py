#!/usr/bin/python3
"""
Unit tests for Rectangle class in rectangle.py
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_area(self):
        """Test the area method."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)


if __name__ == '__main__':
    unittest.main()
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
    
    def test_rectangle_with_id(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.id, 3)

    def test_invalid_rectangle_creation(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

        with self.assertRaises(TypeError):
            Rectangle(1, "2")

        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_area(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)
    
    def test_update_rectangle(self):
        r = Rectangle(1, 2, 3, 4)
        r.update(89)
        self.assertEqual(r.id, 89)

        r.update(89, 1)
        self.assertEqual(r.width, 1)

        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)

