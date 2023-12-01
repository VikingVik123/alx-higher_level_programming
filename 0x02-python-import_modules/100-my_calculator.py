#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Extract arguments
    a, operator, b = sys.argv[1], sys.argv[2], sys.argv[3]

    # Check if a and b can be cast into integers
    try:
        a, b = int(a), int(b)
    except ValueError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Perform the operation based on the operator
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        # Check for division by zero
        if b == 0:
            print("Error: Division by zero is not allowed.")
            sys.exit(1)
        result = a / b
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Print the result
    print("{} {} {} = {}".format(a, operator, b, result))
