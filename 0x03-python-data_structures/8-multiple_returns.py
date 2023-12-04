#!/usr/bin/python3
def multiple_returns(sentence):
     if not sentence:
        return 0, None  # Return (0, None) if the sentence is empty

    length = len(sentence)
    first_char = sentence[0]
    return length, first_char
