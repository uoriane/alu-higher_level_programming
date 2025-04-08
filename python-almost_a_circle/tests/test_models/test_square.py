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

