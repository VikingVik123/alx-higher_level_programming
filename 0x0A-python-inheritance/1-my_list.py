#!/usr/bin/python3

class MyList(list):
    """MyList is a subclass of list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
