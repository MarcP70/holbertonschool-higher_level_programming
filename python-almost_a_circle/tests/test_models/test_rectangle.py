#!/usr/bin/python3
import unittest
import os
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_init(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_init_with_arguments(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_width(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        r1.width = 3
        self.assertEqual(r1.width, 3)
        with self.assertRaises(TypeError):
            r1.width = "test"
        with self.assertRaises(ValueError):
            r1.width = -1

    def test_height(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.height, 2)
        r1.height = 4
        self.assertEqual(r1.height, 4)
        with self.assertRaises(TypeError):
            r1.height = "test"
        with self.assertRaises(ValueError):
            r1.height = -1

    def test_x(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.x, 0)
        r1.x = 3
        self.assertEqual(r1.x, 3)
        with self.assertRaises(TypeError):
            r1.x = "test"
        with self.assertRaises(ValueError):
            r1.x = -1

    def test_y(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.y, 0)
        r1.y = 4
        self.assertEqual(r1.y, 4)
        with self.assertRaises(TypeError):
            r1.y = "test"
        with self.assertRaises(ValueError):
            r1.y = -1

    def test_area(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(4, 5)
        self.assertEqual(r2.area(), 20)

    def test_display(self):
        r1 = Rectangle(2, 3, 1, 1)
        expected_output = "\n" \
                          " ##\n" \
                          " ##\n" \
                          " ##\n"
        captured_output = StringIO()  # Crée un objet StringIO pour capturer la sortie
        sys.stdout = captured_output  # Redirige la sortie standard vers StringIO

        r1.display()  # Exécute la méthode display()

        sys.stdout = sys.__stdout__  # Rétablit la sortie standard
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_args(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1.update(6, 7, 8, 9, 10)
        self.assertEqual(r1.id, 6)
        self.assertEqual(r1.width, 7)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 9)
        self.assertEqual(r1.y, 10)

    def test_update_kwargs(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1.update(id=6, width=7, height=8, x=9, y=10)
        self.assertEqual(r1.id, 6)
        self.assertEqual(r1.width, 7)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 9)
        self.assertEqual(r1.y, 10)

    def test_to_dictionary(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        expected_dict = {
            "id": 5,
            "width": 1,
            "height": 2,
            "x": 3,
            "y": 4
        }
        self.assertDictEqual(r1.to_dictionary(), expected_dict)

    def test_save_to_file(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            json_data = file.read()
            self.assertEqual(json_data,
                             '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}, '
                             '{"id": 10, "width": 6, "height": 7, "x": 8, "y": 9}]')

    def test_load_from_file(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file([r1, r2])
        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 5)
        self.assertEqual(instances[0].width, 1)
        self.assertEqual(instances[0].height, 2)
        self.assertEqual(instances[0].x, 3)
        self.assertEqual(instances[0].y, 4)
        self.assertEqual(instances[1].id, 10)
        self.assertEqual(instances[1].width, 6)
        self.assertEqual(instances[1].height, 7)
        self.assertEqual(instances[1].x, 8)
        self.assertEqual(instances[1].y, 9)

    def test_load_from_file_not_exists(self):
        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), 0)


if __name__ == "__main__":
    unittest.main()
