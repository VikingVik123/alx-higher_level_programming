#!/usr/bin/python3
"""Class with initialization and some conditions"""
class Square:
    def__init__(self, size=0):
        if size < 0:
            ValueError('size must be >= 0')

        elif type(size) is not int:
            TypeError('size must be an integer')

        else:
            self.__size = size

