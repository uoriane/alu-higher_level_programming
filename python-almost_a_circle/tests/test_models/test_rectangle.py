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

