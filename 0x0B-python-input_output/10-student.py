#!/usr/bin/python3
"""Defines a Student class"""

class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get the dictionary representation of the Student
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
