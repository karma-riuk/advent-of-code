from prog import *
import unittest

class Tests(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(result(get_input(sample = True), days = 18), 26)
        self.assertEqual(result(get_input(sample = True)), 5934)

    def test_part2(self):
        self.assertEqual(result(get_input(sample = True), days = 256), 26984457539)

