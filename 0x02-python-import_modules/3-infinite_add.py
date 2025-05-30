#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print('0')
    else:
        sum = 0
        for arg in argv:
            sum = sum + int(arg)
        print(sum)
