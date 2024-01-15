#!/usr/bin/python3
from models.rectangle import Rectangle
"""
Defines a class Square
"""
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width
    """sets property attribute"""
    @size.setter
    def size(self, value):
        self.width = self.height = value

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
