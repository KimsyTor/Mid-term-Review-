import unittest
from pt6 import replace_o


class TestReplaceO(unittest.TestCase):
    def test_replace_o(self):
        self.assertEqual(replace_o("Hello World"), "Hell0 W0rld")
        self.assertEqual(replace_o("foo bar"), "f00 bar")
        self.assertEqual(replace_o("Python is awesome"), "Pyth0n is awes0me")
        self.assertEqual(replace_o("No o's here"), "N0 0's here")
