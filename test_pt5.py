import unittest
from pt5 import count_f


class TestCountF(unittest.TestCase):

    def test_count_f(self):
        text = "f is a letter in the alphabet f and it is use in friendship"
        self.assertEqual(count_f(text), 3)

    def test_count_f_empty(self):
        text = ""
        self.assertEqual(count_f(text), 0)

    def test_count_f_no_f(self):
        text = "This sentence does not contain the letter f"
        self.assertEqual(count_f(text), 1)


if __name__ == '__main__':
    unittest.main()
