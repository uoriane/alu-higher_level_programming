#!/usr/bin/python3
"""
Unit tests for Square class in square.py
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_size(self):
        """Test that size is set correctly."""
        s = Square(5)
        self.assertEqual(s.size, 5)


if __name__ == '__main__':
    unittest.main()
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        s = Square(1)
        self.assertEqual(s.size, 1)
    
    def test_square_with_id(self):
        s = Square(5, 0, 0, 2)
        self.assertEqual(s.id, 2)

    def test_invalid_square_creation(self):
        with self.assertRaises(TypeError):
            Square("1")
        
        with self.assertRaises(TypeError):
            Square(1, "2")
        
        with self.assertRaises(ValueError):
            Square(-1)

    def test_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_update_square(self):
        s = Square(1, 2)
        s.update(89)
        self.assertEqual(s.id, 89)

        s.update(89, 5)
        self.assertEqual(s.size, 5)

