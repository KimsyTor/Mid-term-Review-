import unittest
from pt4 import reverse_list


class TestReverseList(unittest.TestCase):

    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_list([1]), [1])
        self.assertEqual(reverse_list([]), [])
        self.assertEqual(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])
        self.assertEqual(reverse_list([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
