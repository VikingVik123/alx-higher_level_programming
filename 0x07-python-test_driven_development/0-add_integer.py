#!/usr/bin/python3
"""
Create addition function
"""


def add_integer(a, b=98):
    """
    adds a and b
    """
    sum = a + b
    if not isinstance(a, (int, float)):
        raise ValueError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise ValueError("b must be an integer")
    if a is float:
        a_value = int(a)
        return (a_value)
    if b is float:
        b_value = int(b)
        return (b_value)
    return (sum)
