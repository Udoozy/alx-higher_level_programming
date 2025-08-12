#!/usr/bin/python3
"""
This print texts and newline when encountered
a special character as defined
"""


def text_indentation(text):
    """
    Function that perfor the task as decribed above
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_char = ['.', '?', ':']
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in special_char:
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
