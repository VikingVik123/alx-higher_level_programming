#!/usr/bin/python3
from models.base import Base
"""
Defines a class Rectangle
"""
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Call the super class with id"""
        super().__init__(id)

        """Assign each argument width, height, x, and y to the right attribute"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """Public getter and setter for width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")

        self.__width = value

    """Public getter and setter for height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("must be > 0")
        self.__height = value

    """Public getter and setter for x"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """Public getter and setter for y"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Func to calc area"""
        return self.height * self.width
    
    def display(self):
        """ adds the display func"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
    
    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)


    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
