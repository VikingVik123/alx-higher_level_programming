#!/usr/bin/python3
"""Defines a base model class."""
import json


class Base:
    """Base model.
    This class represents the blueprint for all other classes in project 0x0C*.

    Private Class Attribute:
        __nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        obj initialization
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """json to string conv func"""
        """Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries: A list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs: A list of inherited Base instances.
        """
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the deserialization of a JSON string.

        Args:
            json_string: A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    def __str__(self):
        """
        Returns string representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def display(self):
        """
        Prints the Rectangle instance with '#' character considering x and y.
        """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """
        Assigns key/value arguments to attributes.
        Args:
            *args: Non-keyworded arguments. Ignored if **kwargs is present.
            **kwargs: Keyworded arguments representing attribute-value pairs.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
