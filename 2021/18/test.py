from prog import *
import unittest

class Tests(unittest.TestCase):

    def test_eq(self):
        for l in [
                [1,2],
                [[1, 2], 3],
                [[[[[9,8],1],2],3],4],
                [[[[0,9],2],3],4],
                [7,[6,[5,[4,[3,2]]]]],
                [7,[6,[5,[7,0]]]],
                [[6,[5,[4,[3,2]]]],1],
                [[6,[5,[7,0]]],3],
                [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]],
                [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]],
                [[3,[2,[8,0]]],[9,[5,[7,0]]]],
                [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]],
                [[[[0,7],4],[7,[[8,4],9]]],[1,1]],
                [[[[0,7],4],[15,[0,13]]],[1,1]],
                [[[[0,7],4],[[7,8],[0,13]]],[1,1]],
                [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]],
                [[[[0,7],4],[[7,8],[6,0]]],[8,1]],
        ]:
            l1 = parse(l)
            l2 = parse(l)
            with self.subTest(l=l, l1=l1, l2=l2):
                self.assertEqual(l1, l2)

    def test_parse(self):
        for l in [ 
                [1,2],
                [[1, 2], 3],
                [[[[[9,8],1],2],3],4],
                [[[[0,9],2],3],4],
                [7,[6,[5,[4,[3,2]]]]],
                [7,[6,[5,[7,0]]]],
                [[6,[5,[4,[3,2]]]],1],
                [[6,[5,[7,0]]],3],
                [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]],
                [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]],
                [[3,[2,[8,0]]],[9,[5,[7,0]]]],
                [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]],
                [[[[0,7],4],[7,[[8,4],9]]],[1,1]],
                [[[[0,7],4],[15,[0,13]]],[1,1]],
                [[[[0,7],4],[[7,8],[0,13]]],[1,1]],
                [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]],
                [[[[0,7],4],[[7,8],[6,0]]],[8,1]],
        ]:
            with self.subTest(l=l):
                self.assertEqual(parse(l).list(), l)

    def test_explode(self):
        t1 = parse([[[[[9,8],1],2],3],4])
        t1.left_most_pair().explode()
        t2 = parse([[[[0,9],2],3],4])
        self.assertEqual(t1, t2)

        t1 = parse([7,[6,[5,[4,[3,2]]]]])
        t1.right_most_pair().explode()
        t2 = parse([7,[6,[5,[7,0]]]])
        self.assertEqual(t1, t2)

        t1 = parse([[6,[5,[4,[3,2]]]],1])
        t1.left.right_most_pair().explode()
        t2 = parse([[6,[5,[7,0]]],3])
        self.assertEqual(t1, t2)

        t1 = parse([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])
        t1.left.right_most_pair().explode()
        t2 = parse([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
        self.assertEqual(t1, t2)

        t1 = parse([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
        t1.right_most_pair().explode()
        t2 = parse([[3,[2,[8,0]]],[9,[5,[7,0]]]])
        self.assertEqual(t1, t2)

    def test_add_and_reduce(self):
        self.assertEqual(parse([[[[4,3],4],4],[7,[[8,4],9]]]) + parse([1, 1]), parse([[[[0,7],4],[[7,8],[6,0]]],[8,1]]))
        self.assertEqual(parse([[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]) + parse([7,[[[3,7],[4,3]],[[6,3],[8,8]]]]), parse([[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]))
    

    def test_mag(self):
        self.assertEqual(parse([9, 1]).mag(), 29)
        self.assertEqual(parse([1, 9]).mag(), 21)
        self.assertEqual(parse([[9, 1], [1, 9]]).mag(), 129)
        self.assertEqual(parse([[1,2],[[3,4],5]]).mag(), 143)
        self.assertEqual(parse([[[[0,7],4],[[7,8],[6,0]]],[8,1]]).mag(), 1384)
        self.assertEqual(parse([[[[1,1],[2,2]],[3,3]],[4,4]]).mag(), 445)
        self.assertEqual(parse([[[[3,0],[5,3]],[4,4]],[5,5]]).mag(), 791)
        self.assertEqual(parse([[[[5,0],[7,4]],[5,5]],[6,6]]).mag(), 1137)
        self.assertEqual(parse([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]).mag(), 3488)

    # def test_part1_partial(self):
    #     self.assertEqual(result(get_input(sample = True), partial = True), parse([[[[1,1],[2,2]],[3,3]],[4,4]]))
    #     self.assertEqual(result(get_input(sample = True, part = 2), partial = True), parse([[[[3,0],[5,3]],[4,4]],[5,5]]))
    #     self.assertEqual(result(get_input(sample = True, part = 3), partial = True), parse([[[[5,0],[7,4]],[5,5]],[6,6]]))
    #     self.assertEqual(result(get_input(sample = True, part = 4), partial = True), parse([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]))
    #     self.assertEqual(result(get_input(sample = True, part = 5), partial = True), parse([[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]))

    # def test_part1(self):
    #     self.assertEqual(result(get_input(sample = True, part = 5)), 4140)

    # def test_part2(self):
    #     self.assertEqual(result(get_input(sample = True), part = 2), 5)

