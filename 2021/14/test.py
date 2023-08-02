from prog import *
import unittest

def res(s):
    ret = {}
    for i in range(len(s[:-1])):
        sub = s[i] + s[i+1]
        if sub in ret:
            ret[sub] += 1
        else:
            ret[sub] = 1
    return ret

class Tests(unittest.TestCase):
    def test_state(self):
        self.assertEqual(result(get_input(sample = True), steps = 1, ret_state = True), res("NCNBCHB"))
        self.assertEqual(result(get_input(sample = True), steps = 2, ret_state = True), res("NBCCNBBBCBHCB"))
        self.assertEqual(result(get_input(sample = True), steps = 3, ret_state = True), res("NBBBCNCCNBBNBNBBCHBHHBCHB"))
        self.assertEqual(result(get_input(sample = True), steps = 4, ret_state = True), res("NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"))

    def test_len(self):
        self.assertEqual(result(get_input(sample = True), steps = 1, ret_len = True), len("NCNBCHB"))
        self.assertEqual(result(get_input(sample = True), steps = 2, ret_len = True), len("NBCCNBBBCBHCB"))
        self.assertEqual(result(get_input(sample = True), steps = 3, ret_len = True), len("NBBBCNCCNBBNBNBBCHBHHBCHB"))
        self.assertEqual(result(get_input(sample = True), steps = 4, ret_len = True), len("NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"))

    def test_part1(self):
        self.assertEqual(result(get_input(sample = True)), 1588)

    def test_part2(self):
        self.assertEqual(result(get_input(sample = True), part = 2, steps = 40), 2188189693529)

