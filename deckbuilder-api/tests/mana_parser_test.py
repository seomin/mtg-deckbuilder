import unittest

from util import mana_parser


class TestStatistics(unittest.TestCase):

    def test_it(self):
        cost = mana_parser.parse("{3}{X}{W}{B}{B}")
        self.assertEqual(1, cost["W"])
        self.assertEqual(2, cost["B"])
        self.assertEqual(3, cost["colorless"])
        self.assertEqual(0, cost["U"])
        self.assertEqual(0, cost["R"])
        self.assertEqual(0, cost["G"])
