#!/usr/bin/python3
"""
Sample test file to confirm tests setup works.
"""

import unittest


class TestSample(unittest.TestCase):
    """
    Sample test case to validate test setup.
    """

    def test_pass(self):
        """Test that always passes."""
        self.assertEqual(1 + 1, 2)


if __name__ == '__main__':
    unittest.main()

