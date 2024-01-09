#!/usr/bin/python3
"""Defines an inherited class-checking function."""

def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class
    that inherited
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
