import unittest

from util import color_parser


class TestStatistics(unittest.TestCase):

    def test_it(self):
        cost = color_parser.parse("{3}{W}{B}{B}")
        self.assertEqual(1, cost["W"])
        self.assertEqual(2, cost["B"])
        self.assertEqual(3, cost["colorless"])
