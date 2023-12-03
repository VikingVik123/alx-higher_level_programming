#!/usr/bin/python3
def no_c(my_string):
    result = ''.join(char for char in my_string if char.lower() not in {'c', 'C'})
    return result
