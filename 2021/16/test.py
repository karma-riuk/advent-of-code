from prog import *
import unittest

class Tests(unittest.TestCase):

    def test_pack1(self):
        pack = 0xD2FE28
        s = full_size(pack)
        self.assertEqual(full_size(pack), 24)
        self.assertEqual(version(pack, s), 6)
        self.assertEqual(type(pack, s), 4)
        self.assertEqual(literal(pack, s), 2021)

    def test_pack2(self):
        pack = 0x38006F45291200
        s = full_size(pack)
        self.assertEqual(full_size(pack), 56)
        self.assertEqual(version(pack, s), 1)
        self.assertEqual(type(pack, s), 6)
        self.assertEqual(type_id(pack, s), 0)
        self.assertEqual(len_subpackets(pack, s), 27)

    def test_pack3(self):
        pack = 0xEE00D40C823060
        s = full_size(pack)
        self.assertEqual(full_size(pack), 56)
        self.assertEqual(version(pack, s), 7)
        self.assertEqual(type(pack, s), 3)
        self.assertEqual(type_id(pack, s), 1)
        self.assertEqual(n_subpackets(pack, s), 3)

    def test_part1(self):
        self.assertEqual(result(0x8A004A801A8002F478), 16)
        self.assertEqual(result(0x620080001611562C8802118E34), 12)
        self.assertEqual(result(0xC0015000016115A2E0802F182340), 23)
        self.assertEqual(result(0xA0016C880162017C3686B18A3D4780), 31)

    def test_part2(self):
        self.assertEqual(result(0xC200B40A82, part = 2), 3)
        self.assertEqual(result(0x880086C3E88112, part = 2), 7)
        self.assertEqual(result(0xCE00C43D881120, part = 2), 9)
        self.assertEqual(result(0xD8005AC2A8F0, part = 2), 1)
        self.assertEqual(result(0xF600BC2D8F, part = 2), 0)
        self.assertEqual(result(0x9C005AC2F8F0, part = 2), 0)
        self.assertEqual(result(0x9C0141080250320F1802104A08, part = 2), 1)

    def test_spec(self):
        self.assertEqual(result(0x04005AC33890, part = 2), 54)
        
