from prog import *
import unittest

class Tests(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(result(get_input(sample = True)), 10)
        self.assertEqual(result(get_input(sample = True, part = 2)), 19)
        self.assertEqual(result(get_input(sample = True, part = 3)), 226)

    def test_sol1(self):
        self.assertEqual(result(get_input()), 3497)


    def test_part2(self):
        self.assertEqual(result(get_input(sample = True), part = 2), 36)
        self.assertEqual(result(get_input(sample = True, part = 2), part = 2), 103)
        self.assertEqual(result(get_input(sample = True, part = 3), part = 2), 3509)

