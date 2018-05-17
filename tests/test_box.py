import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from box import box
from handler import handler

class TestBox(unittest.TestCase):

    def test_raises_exception_with_bad_arguments(self):
        with self.assertRaises(Exception):
            box(length=0, width=0, height=0)

    def test_creates_box_with_valid_arguments(self):
        result = box(1, 1, 1)
        print(result)
     
if __name__ == '__main__':
    unittest.main()