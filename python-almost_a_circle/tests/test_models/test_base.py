#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        if os.path.exists("Base.json"):
            os.remove("Base.json")

    def test_init_with_id(self):
        b1 = Base(1)
        self.assertEqual(b1.id, 1)

    def test_init_without_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_init_id_none(self):
        b1 = Base(None)
        self.assertEqual(b1.id, 1)

    def test_init_with_id_string(self):
        b1 = Base("test")
        self.assertEqual(b1.id, "test")

    def test_init_with_id_negative(self):
        b1 = Base(-3)
        self.assertEqual(b1.id, -3)

    def test_init_with_id_float(self):
        b1 = Base(4.3)
        self.assertEqual(b1.id, 4.3)

    def test_to_json_string_empty(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_none(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_to_json_string(self):
        objs = [{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]
        json_str = Base.to_json_string(objs)
        self.assertEqual(json_str, '[{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]')

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            json_data = file.read()
            self.assertEqual(json_data, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]')

    def test_save_to_file_empty(self):
        Base.save_to_file([])
        self.assertTrue(os.path.exists("Base.json"))
        with open("Base.json", "r") as file:
            json_data = file.read()
            self.assertEqual(json_data, "[]")

    def test_from_json_string_empty(self):
        json_list = Base.from_json_string("[]")
        self.assertEqual(json_list, [])

    def test_from_json_string_none(self):
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])

    def test_from_json_string(self):
        json_str = '[{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]'
        json_list = Base.from_json_string(json_str)
        self.assertEqual(json_list, [{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}])

    def test_create_rectangle(self):
        rect_dict = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        r = Rectangle.create(**rect_dict)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_create_square(self):
        sq_dict = {"id": 1, "size": 2, "x": 3, "y": 4}
        s = Square.create(**sq_dict)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_load_from_file_not_exists(self):
        with open("Square.json", "w") as file:
            pass
        instances = Square.load_from_file()
        self.assertEqual(len(instances), 0)
        os.remove("Square.json")

    def test_load_from_file_exists(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        instances = Square.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)



if __name__ == "__main__":
    unittest.main()
