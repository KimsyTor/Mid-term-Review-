import unittest
from pt1 import add_if_even


class TestAddIfEven(unittest.TestCase):

    def test_add_if_even(self):
        self.assertEqual(add_if_even([1, 2, 3, 4, 5]), [1, 2, 10, 3, 4, 10, 5])
        self.assertEqual(add_if_even([2, 4, 6, 8]), [
                         2, 10, 4, 10, 6, 10, 8, 10])
        self.assertEqual(add_if_even([1, 3, 5]), [1, 3, 5])
        self.assertEqual(add_if_even([]), [])
        self.assertEqual(add_if_even([2]), [2, 10])


if __name__ == '__main__':
    unittest.main()
