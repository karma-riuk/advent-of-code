import unittest
from prog import *

class Rotate(unittest.TestCase):
    def test_rotate_L90(self):
        self.assertEqual(new_dir_after_rotate("N", "L", 90), "W")
        self.assertEqual(new_dir_after_rotate("E", "L", 90), "N")
        self.assertEqual(new_dir_after_rotate("S", "L", 90), "E")
        self.assertEqual(new_dir_after_rotate("W", "L", 90), "S")

    def test_rotate_R90(self):
        self.assertEqual(new_dir_after_rotate("N", "R", 90), "E")
        self.assertEqual(new_dir_after_rotate("E", "R", 90), "S")
        self.assertEqual(new_dir_after_rotate("S", "R", 90), "W")
        self.assertEqual(new_dir_after_rotate("W", "R", 90), "N")

    def test_rotate_L180(self):
        self.assertEqual(new_dir_after_rotate("N", "L", 180), "S")
        self.assertEqual(new_dir_after_rotate("E", "L", 180), "W")
        self.assertEqual(new_dir_after_rotate("S", "L", 180), "N")
        self.assertEqual(new_dir_after_rotate("W", "L", 180), "E")

    def test_rotate_R180(self):
        self.assertEqual(new_dir_after_rotate("N", "R", 180), "S")
        self.assertEqual(new_dir_after_rotate("E", "R", 180), "W")
        self.assertEqual(new_dir_after_rotate("S", "R", 180), "N")
        self.assertEqual(new_dir_after_rotate("W", "R", 180), "E")

    def test_rotate_L270(self):
        self.assertEqual(new_dir_after_rotate("N", "L", 270), "E")
        self.assertEqual(new_dir_after_rotate("E", "L", 270), "S")
        self.assertEqual(new_dir_after_rotate("S", "L", 270), "W")
        self.assertEqual(new_dir_after_rotate("W", "L", 270), "N")

    def test_rotate_R270(self):
        self.assertEqual(new_dir_after_rotate("N", "R", 270), "W")
        self.assertEqual(new_dir_after_rotate("E", "R", 270), "N")
        self.assertEqual(new_dir_after_rotate("S", "R", 270), "E")
        self.assertEqual(new_dir_after_rotate("W", "R", 270), "S")

    def test_rotate_L360(self):
        self.assertEqual(new_dir_after_rotate("N", "L", 360), "N")
        self.assertEqual(new_dir_after_rotate("E", "L", 360), "E")
        self.assertEqual(new_dir_after_rotate("S", "L", 360), "S")
        self.assertEqual(new_dir_after_rotate("W", "L", 360), "W")

    def test_rotate_R360(self):
        self.assertEqual(new_dir_after_rotate("N", "R", 360), "N")
        self.assertEqual(new_dir_after_rotate("E", "R", 360), "E")
        self.assertEqual(new_dir_after_rotate("S", "R", 360), "S")
        self.assertEqual(new_dir_after_rotate("W", "R", 360), "W")

class Result(unittest.TestCase):
    def setUp(self):
        self.inp = get_input(sample = True)

    def test_part_1(self):
        result = get_result(self.inp)
        self.assertEqual(result, 25)

    def test_part_2(self):
        result = get_result(self.inp, part = 2)
        self.assertEqual(result, 286)

