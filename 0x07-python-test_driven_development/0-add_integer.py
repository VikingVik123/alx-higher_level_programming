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
        return(a_value)
    if b is float:
        b_value = int(b)
        return(b_value)
    return(sum)

if __name__ == "__main__":
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)