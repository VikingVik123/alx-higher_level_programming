#!/usr/bin/python3
from models.rectangle import Rectangle
"""
Defines a class Square
"""
class Square(Rectangle):
    """
    Created a class square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialization
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Defines the size of the square"""
        return self.width
    """sets property attribute"""
    @size.setter
    def size(self, value):
        self.width = self.height = value

    def to_dictionary(self):
        """returns dict rep of the square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
