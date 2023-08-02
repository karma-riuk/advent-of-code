from prog import *
import unittest

class Tests(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(result(get_input(True)), 150)

    def test_part2(self):
        self.assertEqual(result(get_input(True), 2), 900)

