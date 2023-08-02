from prog import *
import unittest

class Methods(unittest.TestCase):
    pass

class Result(unittest.TestCase):
    def test_p1(self):
        inp = get_input(sample = True)
        self.assertEqual(get_result(self.inp), 71)

    def test_p2(self):
        inp = get_input(sample = True, part = 2)
        self.assertEqual(get_result(inp, part = 2), 71)
    
