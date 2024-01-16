#!/usr/bin/python3
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):

    def test_instance_creation(self):
        base_instance = Base()
        self.assertIsInstance(base_instance, Base)
        self.assertTrue(hasattr(base_instance, 'id'))

    def test_instance_id_increment(self):
        base_instance1 = Base()
        base_instance2 = Base()
        self.assertEqual(base_instance1.id, 1)
        self.assertEqual(base_instance2.id, 2)

    def test_custom_id(self):
        base_instance = Base(100)
        self.assertEqual(base_instance.id, 100)

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_non_empty_list(self):
        base_instance1 = Base()
        base_instance2 = Base()
        json_string = Base.to_json_string([base_instance1.to_dictionary(), base_instance2.to_dictionary()])
        expected_result = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(json_string, expected_result)

    def test_from_json_string_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_non_empty_string(self):
        json_string = '[{"id": 1}, {"id": 2}]'
        list_of_dicts = Base.from_json_string(json_string)
        expected_result = [{'id': 1}, {'id': 2}]
        self.assertEqual(list_of_dicts, expected_result)

    def test_save_to_file(self):
        base_instance1 = Base()
        base_instance2 = Base()
        Base.save_to_file([base_instance1, base_instance2])
        with open('Base.json', 'r') as file:
            json_content = file.read()
        expected_result = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(json_content, expected_result)

if __name__ == '__main__':
    unittest.main()
