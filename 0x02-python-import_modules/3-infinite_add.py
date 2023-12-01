#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Check if there are arguments
    if len(sys.argv) > 1:
        # Summing all command-line arguments
        result = sum(int(arg) for arg in sys.argv[1:])
        
        # Printing the result
        print(result)
    else:
        # No arguments provided
        print("No arguments provided.")
