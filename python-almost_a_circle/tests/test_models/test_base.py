#!/usr/bin/python3
"""
Unit tests for Base class in base.py
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_id_assignment(self):
        """Test automatic and manual id assignment."""
        b1 = Base()
        b2 = Base()
        b3 = Base(89)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 89)


if __name__ == '__main__':
    unittest.main()

