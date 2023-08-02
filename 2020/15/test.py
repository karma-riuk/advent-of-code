from prog import *
import unittest

class Methods(unittest.TestCase):
    pass
    
class Result(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(get_result([0, 3, 6]), 436)
        self.assertEqual(get_result([1, 3, 2]), 1)
        self.assertEqual(get_result([2, 1, 3]), 10)
        self.assertEqual(get_result([1, 2, 3]), 27)
        self.assertEqual(get_result([2, 3, 1]), 78)
        self.assertEqual(get_result([3, 2, 1]), 438)
        self.assertEqual(get_result([3, 1, 2]), 1836)

        
    def test_p2_1(self):
        self.assertEqual(get_result([0, 3, 6], part = 2), 175594)
    def test_p2_2(self):
        self.assertEqual(get_result([1, 3, 2], part = 2), 2578)
    def test_p2_3(self):
        self.assertEqual(get_result([2, 1, 3], part = 2), 3544142)
    def test_p2_4(self):
        self.assertEqual(get_result([1, 2, 3], part = 2), 261214)
    def test_p2_5(self):
        self.assertEqual(get_result([2, 3, 1], part = 2), 6895259)
    def test_p2_6(self):
        self.assertEqual(get_result([3, 2, 1], part = 2), 18)
    def test_p2_7(self):
        self.assertEqual(get_result([3, 1, 2], part = 2), 362)
