#!/usr/bin/python3
"""
Function that writes to stdout
"""
def write_file(filename="", text=""):
    """
    write a file to stdout
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return(f.write(text))
