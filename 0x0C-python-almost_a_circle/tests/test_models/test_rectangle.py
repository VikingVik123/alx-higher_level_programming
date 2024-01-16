#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    """Creates test class"""

    def test_instance_creation(self):
        """tests for rec creation"""
        rect_instance = Rectangle(5, 3, 2, 1, 1)
        self.assertIsInstance(rect_instance, Rectangle)
        self.assertTrue(hasattr(rect_instance, 'id'))
        self.assertTrue(hasattr(rect_instance, 'width'))
        self.assertTrue(hasattr(rect_instance, 'height'))
        self.assertTrue(hasattr(rect_instance, 'x'))
        self.assertTrue(hasattr(rect_instance, 'y'))

    def test_default_id_increment(self):
        """tests for id increment"""
        rect_instance1 = Rectangle(5, 3, 2, 1)
        rect_instance2 = Rectangle(10, 2, 1, 9)
        self.assertEqual(rect_instance1.id, 1)
        self.assertEqual(rect_instance2.id, 2)

    def test_custom_id(self):
        rect_instance = Rectangle(5, 3, 2, 1, 100)
        self.assertEqual(rect_instance.id, 100)

if __name__ == '__main__':
    unittest.main()

