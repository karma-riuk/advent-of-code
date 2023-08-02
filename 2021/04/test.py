from prog import *
import unittest

class Tests(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(result(get_input(sample = True)), 4512)
        self.assertEqual(result(get_input()), 44736)

    def test_part2(self):
        self.assertEqual(result(get_input(sample = True), part = 2), 1924)

