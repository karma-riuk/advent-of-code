from prog import *
import unittest

class Methods(unittest.TestCase):
    def test_get_input(self):
        inp = get_input(sample = True)
        self.assertEqual(inp, [939, [7, 13, 'x', 'x', 59, 'x', 31, 19]])

class Result(unittest.TestCase):
    def setUp(self):
        self.inp = get_input(sample = True)

    def test_part_1(self):
        self.assertEqual(get_result(self.inp), 295)

    def test_part_2(self):
        self.assertEqual(get_result([0, [7, 13]], part = 2), 77)
        self.assertEqual(get_result([0, [17, 'x', 13, 19]], part = 2), 3417)
        self.assertEqual(get_result(self.inp, part = 2), 1068781)

