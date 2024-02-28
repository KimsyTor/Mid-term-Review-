import unittest
from pt3 import sum_odd


class TestSumOdd(unittest.TestCase):

    def test_sum_odd(self):
        self.assertEqual(sum_odd([1, 2, 3, 4, 5]), 9)
        self.assertEqual(sum_odd([0, 1, 2, 3, 4, 5]), 9)
        self.assertEqual(sum_odd([2, 4, 6]), 0)
        self.assertEqual(sum_odd([1]), 1)
        self.assertEqual(sum_odd([]), 0)


if __name__ == '__main__':
    unittest.main()
