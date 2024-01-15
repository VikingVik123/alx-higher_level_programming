#!/usr/bin/python3
from models.base import Base
"""
Defines a class Rectangle
"""

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
    """Call the super class with id to use the logic of the __init__ of the Base class"""
        super().__init__(id)

        """Assign each argument width, height, x, and y to the right attribute"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ Public getter and setter for width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    """ Public getter and setter for height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    """ Public getter and setter for x"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    """Public getter and setter for y"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
