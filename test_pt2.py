import unittest
from pt2 import remove_duplicate


class TestRemoveDuplicate(unittest.TestCase):
    def test_remove_duplicate(self):
        self.assertEqual(remove_duplicate([1, 2, 3, 5, 1, 2, 4, 5]), [3, 4])
        self.assertEqual(remove_duplicate([1, 1, 1, 1]), [])
        self.assertEqual(remove_duplicate([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(remove_duplicate([]), [])


if __name__ == '__main__':
    unittest.main()
