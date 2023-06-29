#!/usr/bin/python3
import unittest
import os
import sys
from io import StringIO
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_init(self):
        s1 = Square(2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_init_with_arguments(self):
        s1 = Square(2, 3, 4, 5)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

    def test_size(self):
        s1 = Square(2)
        self.assertEqual(s1.size, 2)
        s1.size = 3
        self.assertEqual(s1.size, 3)
        with self.assertRaises(TypeError):
            s1.size = "test"
        with self.assertRaises(ValueError):
            s1.size = -1

    def test_x(self):
        s1 = Square(2)
        self.assertEqual(s1.x, 0)
        s1.x = 3
        self.assertEqual(s1.x, 3)
        with self.assertRaises(TypeError):
            s1.x = "test"
        with self.assertRaises(ValueError):
            s1.x = -1

    def test_y(self):
        s1 = Square(2)
        self.assertEqual(s1.y, 0)
        s1.y = 4
        self.assertEqual(s1.y, 4)
        with self.assertRaises(TypeError):
            s1.y = "test"
        with self.assertRaises(ValueError):
            s1.y = -1

    def test_area(self):
        s1 = Square(2)
        self.assertEqual(s1.area(), 4)
        s2 = Square(4)
        self.assertEqual(s2.area(), 16)

    def test_display(self):
        s1 = Square(2, 1, 1)
        expected_output = "\n" \
                          " ##\n" \
                          " ##\n"
        captured_output = StringIO()  # Crée un objet StringIO pour capturer la sortie
        sys.stdout = captured_output  # Redirige la sortie standard vers StringIO

        s1.display()  # Exécute la méthode display()

        sys.stdout = sys.__stdout__  # Rétablit la sortie standard
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        s1 = Square(2, 3, 4, 5)
        self.assertEqual(str(s1), "[Square] (5) 3/4 - 2")

    def test_update_args(self):
        s1 = Square(2, 3, 4, 5)
        s1.update(6, 7, 8, 9)
        self.assertEqual(s1.id, 6)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.x, 8)
        self.assertEqual(s1.y, 9)

    def test_update_kwargs(self):
        s1 = Square(2, 3, 4, 5)
        s1.update(id=6, size=7, x=8, y=9)
        self.assertEqual(s1.id, 6)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.x, 8)
        self.assertEqual(s1.y, 9)

    def test_to_dictionary(self):
        s1 = Square(2, 3, 4, 5)
        expected_dict = {
            "id": 5,
            "size": 2,
            "x": 3,
            "y": 4
        }
        self.assertDictEqual(s1.to_dictionary(), expected_dict)

    def test_save_to_file(self):
        s1 = Square(2, 3, 4, 5)
        s2 = Square(6, 7, 8, 9)
        Square.save_to_file([s1, s2])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as file:
            json_data = file.read()
            self.assertEqual(json_data,
                             '[{"id": 5, "size": 2, "x": 3, "y": 4}, '
                             '{"id": 9, "size": 6, "x": 7, "y": 8}]')

    def test_load_from_file(self):
        s1 = Square(2, 3, 4, 5)
        s2 = Square(6, 7, 8, 9)
        Square.save_to_file([s1, s2])
        instances = Square.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 5)
        self.assertEqual(instances[0].size, 2)
        self.assertEqual(instances[0].x, 3)
        self.assertEqual(instances[0].y, 4)
        self.assertEqual(instances[1].id, 9)
        self.assertEqual(instances[1].size, 6)
        self.assertEqual(instances[1].x, 7)
        self.assertEqual(instances[1].y, 8)

    def test_load_from_file_not_exists(self):
        instances = Square.load_from_file()
        self.assertEqual(len(instances), 0)


if __name__ == "__main__":
    unittest.main()
