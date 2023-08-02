from prog import *
import unittest

class Methods(unittest.TestCase):
    def test_bracket(self):
        self.assertEqual(find_closing_bracket_starting_at(4, "1 + (1 + 2)"), 10)
        self.assertEqual(find_closing_bracket_starting_at(0, "(1 + 2)"), 6)
        self.assertEqual(find_closing_bracket_starting_at(1, "((1 + 2) + 2)"), 7)
        self.assertEqual(find_closing_bracket_starting_at(0, "((1 + 2) + 2)"), 12)

    def test_evaluate_l2r_simple(self):
        self.assertEqual(evaluate_l2r("1 + 1"), 2)
        self.assertEqual(evaluate_l2r("51 + 24"), 75)
        self.assertEqual(evaluate_l2r("223 * 23"), 5129)

    def test_evaluate_adv_simple(self):
        self.assertEqual(evaluate_advanced("1 + 1"), 2)
        self.assertEqual(evaluate_advanced("51 + 24"), 75)
        self.assertEqual(evaluate_advanced("223 * 23"), 5129)

    def test_evaluate_l2r_medium(self):
        self.assertEqual(evaluate_l2r("1 + 1 + 1"), 3)
        self.assertEqual(evaluate_l2r("12 + 278 + 3"), 293)
        self.assertEqual(evaluate_l2r("22 * 2 + 1"), 45)
        self.assertEqual(evaluate_l2r("3 + 2 * 10"), 50)

    def test_evaluate_adv_medium(self):
        self.assertEqual(evaluate_advanced("11 + 12 + 13 * 21 + 22 * 31 + 32 + 33 + 34"), 201240)
        self.assertEqual(evaluate_advanced("12 + 278 + 3"), 293)
        self.assertEqual(evaluate_advanced("22 * 2 + 1"), 66)
        self.assertEqual(evaluate_advanced("3 + 2 * 10"), 50)

    def test_evaluate_l2r_hard(self):
        self.assertEqual(evaluate_l2r("2 * 3 + (4 * 5)"), 26)
        self.assertEqual(evaluate_l2r("5 + (8 * 3 + 9 + 3 * 4 * 3)"), 437)
        self.assertEqual(evaluate_l2r("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"), 12240)
        self.assertEqual(evaluate_l2r("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"), 13632)

    def test_evaluate_adv_hard(self):
        self.assertEqual(evaluate_advanced("3 * 3 + (1 * 1 * 1)"), 12)
        self.assertEqual(evaluate_advanced("1 + (2 * 3) + (4 * (5 + 6))"), 51)
        self.assertEqual(evaluate_advanced("2 * 3 + (4 * 5)"), 46)
        self.assertEqual(evaluate_advanced("5 + (8 * 3 + 9 + 3 * 4 * 3)"), 1445)
        self.assertEqual(evaluate_advanced("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"), 669060)
        self.assertEqual(evaluate_advanced("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"), 23340)

class Result(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(get_result(get_input(sample = True)), 26335)

    def test_p2(self):
        self.assertEqual(get_result(get_input(sample = True, part = 2), part = 2), 693942)
        

