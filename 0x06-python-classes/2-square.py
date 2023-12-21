#!/usr/bin/python3
"""Class with initialization and some conditions"""
class Square:
    def__init__(self, size=0):
        """object initialization"""
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if size < 0:
            """condition to ensure non - value"""
            ValueError('size must be >= 0')

        elif type(size) is not int:
            """condition 2 ensure int value"""
            TypeError('size must be an integer')

        else:
            self.__size = size
