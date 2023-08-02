from prog import *
import unittest

class Methods(unittest.TestCase):
    def test_parse_masks(self):
        self.assertEqual(
                parse_masks("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"),
                (
                    0b111111111111111111111111111111111101,
                    0b000000000000000000000000000001000000
                    )
                )

        self.assertEqual(
                parse_masks("XXXXXXXXX1XXXXXXXX1X0XXXXXXXX1XXXX0X"),
                (
                    0b111111111111111111110111111111111101,
                    0b000000000100000000100000000001000000
                    )
                )

        self.assertEqual(
                parse_masks("XXXXX11XXXX1XX000XX0XXXXXXXXX1XXXX0X"),
                (
                    0b111111111111110001101111111111111101,
                    0b000001100001000000000000000001000000
                    )
                )

    def test_decode_memory(self):
        mask = "000000000000000000000000000000X1001X"
        self.assertEqual(decode_memory_address(42, mask), {26, 27, 58, 59})

        mask = "00000000000000000000000000000000X0XX"
        self.assertEqual(decode_memory_address(26, mask), {16, 17, 18, 19, 24, 25, 26, 27})

class Result(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(get_result(get_input(sample = True, sample_n = 1)), 165)

    def test_part2(self):
        self.assertEqual(get_result(get_input(sample = True, sample_n = 2), part = 2), 208)
