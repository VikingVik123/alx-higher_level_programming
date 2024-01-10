#!/usr/bin/python3
"""Defines a function for file reading."""

def read_file(filename=""):
    """
    prints contents of file 2 stdout
    """
    with open(filename,'r', encoding= "uft=8")as f:
        print(f.read(), end="")
