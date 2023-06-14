#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_positive_numbers(self):
        result = max_integer([10, 5, 8, 3, 15, 12])
        self.assertEqual(result, 15)

    def test_negative_numbers(self):
        result = max_integer([-5, -10, -3, -1, -8])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([-5, 10, -3, 0, 8])
        self.assertEqual(result, 10)

    def test_duplicate_numbers(self):
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'a', 4, 5])


if __name__ == '__main__':
    unittest.main()
