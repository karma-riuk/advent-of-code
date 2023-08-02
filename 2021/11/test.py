from prog import *
import unittest

class Tests(unittest.TestCase):
    def test_part1_grid(self):
        self.assertEqual(result([
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1],
        ], grid = True, steps = 1), [
            [3, 4, 5, 4, 3],
            [4, 0, 0, 0, 4],
            [5, 0, 0, 0, 5],
            [4, 0, 0, 0, 4],
            [3, 4, 5, 4, 3],
        ])

        self.assertEqual(result([
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1],
        ], grid = True, steps = 2), [
            [4, 5, 6, 5, 4],
            [5, 1, 1, 1, 5],
            [6, 1, 1, 1, 6],
            [5, 1, 1, 1, 5],
            [4, 5, 6, 5, 4],
        ])



    def test_part1(self):

        self.assertEqual(result([
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1],
        ], steps = 1), 9)


        self.assertEqual(result([
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1],
        ], steps = 2), 9)


        self.assertEqual(result(get_input(sample = True), steps = 10), 204)
        self.assertEqual(result(get_input(sample = True)), 1656)

    def test_part2(self):
        self.assertEqual(result(get_input(sample = True), part = 2), 195)

