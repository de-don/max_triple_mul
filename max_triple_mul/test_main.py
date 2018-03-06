from unittest import TestCase

from .main import ListSmallSize, max_triple_mul


class TestMaxTripleProd(TestCase):
    """ Test for function max_triple_mul """

    def test_exception(self):
        """ small sized lists """
        with self.assertRaises(ListSmallSize):
            max_triple_mul([1, 2])

    def test_three_positive(self):
        """ lists with only three positive items"""
        result = max_triple_mul([1, 2, 3])
        self.assertEqual(result, 6)

        result = max_triple_mul([2, 3, 4])
        self.assertEqual(result, 24)

    def test_zero(self):
        """ when function should return zero """
        result = max_triple_mul([1, 2, 0])
        self.assertEqual(result, 0)

    def test_with_negative(self):
        """ list contains positive, negative and zero values """
        inp = [5, 6, 7, -100, -10, 0]
        result = max_triple_mul(inp)

        self.assertEqual(result, 7000)
        self.assertNotEqual(result, 210)

    def test_many_positive(self):
        """ different test with positive and negative """

        # pairs (input, result)
        pairs = [
            ([3, 4, 6, 8, 0], 192),
            ([1, -1, 1, -1, 1], 1),
            ([0, 0, 0, 0, -1], 0),
            ([6, 5, 4, 3, 2], 120),
            ([6, 5, 4, 3, -2], 120),
            ([6, 5, 4, -3, -2], 120),
            ([-6, -5, 4, 3, 0], 120),
            ([-6, 5, 4, 3, 2], 60),
            ([5, 6, -100, -1, 10], 1000)
        ]

        for lst, result in pairs:
            self.assertEqual(max_triple_mul(lst), result)
