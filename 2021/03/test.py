from prog import *
import unittest

class Tests(unittest.TestCase):
    def test_input(self):
        self.assertEqual(get_input(sample = True), [4, 30, 22, 23, 21, 15, 7, 28, 16, 25, 2, 10])
        
    def test_part1(self):
        self.assertEqual(result(get_input(sample = True)), 198)

    def test_part2(self):
        self.assertEqual(result(get_input(sample = True), part = 2), 230)

