#!/usr/bin/python3
"""
Defines a text file insertion function
"""

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each line containing the search_string.

    Returns:
        None
    """
    # Open the file in read mode and create a temporary list to store modified lines
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Open the file in write mode to overwrite the existing content
    with open(filename, 'w') as file:
        # Iterate through the lines and append the new_string after matching lines
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
