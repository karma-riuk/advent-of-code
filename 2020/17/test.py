from prog import *
import unittest

class Methods(unittest.TestCase):
    pass

class Result(unittest.TestCase):
    def setUp(self):
        self.inp = get_input(sample = True)

    def test_p1(self):
        self.assertEqual(get_result(self.inp), 112)

    def test_p2(self):
        self.assertEqual(get_result(self.inp, part = 2), 848)
        
