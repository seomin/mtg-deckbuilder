import unittest

from db import color_parser


class TestStatistics(unittest.TestCase):

    def test_it(self):
        cost = color_parser.parse("{W}")
        self.assertEqual(1, cost["W"])
