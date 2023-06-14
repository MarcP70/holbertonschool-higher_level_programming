#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list_unordered(self):
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -4, -3, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -4, -3, -2]), 1)

    def test_duplicated_numbers(self):
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_float_list(self):
        self.assertEqual(max_integer([1.2, 4.1, 3.6, 2.2]), 4.1)

    def test_isnone(self):
        with self.assertRaises(TypeError):
            max_integer(None)
            
    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'a', 4, 5])


if __name__ == '__main__':
    unittest.main()
