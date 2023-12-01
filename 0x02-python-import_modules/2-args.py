#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Get the number of arguments
    num_arguments = len(sys.argv) - 1  # Subtract 1 to exclude the script name

    # Print the number of arguments and their list
    if num_arguments == 0:
        print("Number of argument(s): 0.")
    elif num_arguments == 1:
        print("Number of argument(s): 1.")
        print("1: {}".format(sys.argv[1]))
    else:
        print("Number of argument(s): {}.".format(num_arguments))
        for i in range(1, num_arguments + 1):
            print("{}: {}".format(i, sys.argv[i]))
