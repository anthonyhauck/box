import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from box import box

class TestBox(unittest.TestCase):

    def test_raises_exception_with_bad_arguments(self):
        with self.assertRaises(Exception):
            box(length=0, width=0, height=0)

    def test_creates_box_with_valid_arguments(self):
        result = box(1, 1, 1)
        self.assertIsNotNone(result['model'])
        self.assertIsNotNone(result['computed'])
        self.assertEqual(result['computed']['volume'], 1)