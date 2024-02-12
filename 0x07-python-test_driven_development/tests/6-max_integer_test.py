#!/usr/bin/python3
import unittest
import sys

sys.path.append("../")
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger (unittest.TestCase):
    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_values(self):
        self.assertEqual(max_integer([3, 9, 4, 1, 2]), 9)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 1, 1]), 1)
