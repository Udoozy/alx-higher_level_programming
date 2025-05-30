#!/usr/bin/env python3

if __name__ == '__main__':
    import sys

    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print(f"{argc} arguments:")

    i = 1
    for arg in argv:
        print(f"{i}: {arg}")
        i += 1
